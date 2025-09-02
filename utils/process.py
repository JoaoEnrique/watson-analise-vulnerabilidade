from fastapi import FastAPI, UploadFile, File
import os
from utils.parser_utils import parse_file
from collections import Counter, defaultdict
import json
from utils.vars import EXAMPLES
from utils.watson import model

async def save_upload(file_input: UploadFile, folder="uploads") -> str:
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, file_input.filename)
    with open(file_path, "wb") as f:
        f.write(await file_input.read())
    return file_path


def parse_cve_file(file_path: str):
    data = parse_file(file_path)
    try:
        return json.loads(data)["vulnerabilities"]
    except KeyError as e:
        raise ValueError(f"Chave faltando no arquivo: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro ao decodificar JSON: {e}")

def calculate_statistics(cves):
    from collections import Counter
    years = Counter()
    types = Counter()
    severities = Counter()

    for item in cves:
        cve_data = item.get("cve", {})
        years[cve_data.get("published", "0000")[:4]] += 1

        weaknesses = cve_data.get("weaknesses", [])
        if weaknesses and "description" in weaknesses[0]:
            cwe_desc = weaknesses[0]["description"]
            if cwe_desc:
                types[cwe_desc[0].get("value", "Unknown")] += 1

        metrics = cve_data.get("metrics", {})
        if "cvssMetricV31" in metrics and metrics["cvssMetricV31"]:
            score = metrics["cvssMetricV31"][0]["cvssData"].get("baseScore")
            if score is not None:
                severities[str(score)] += 1
        elif "cvssMetricV2" in metrics and metrics["cvssMetricV2"]:
            score = metrics["cvssMetricV2"][0]["cvssData"].get("baseScore")
            if score is not None:
                severities[str(score)] += 1

    return dict(years), dict(types.most_common(10)), dict(severities)

# def generate_watson_summary(cves, examples=EXAMPLES):
#     prompt_input = f"{examples}\nEntrada: {json.dumps(cves[:5])}\nSaída:"
#     response = model.generate_text(prompt=prompt_input, guardrails=False)
#     return response.split("Entrada")[0].strip()


def generate_watson_summary(cves, examples=EXAMPLES):
    years, types, severities = calculate_statistics(cves) # extrai estatísticas

    summary_input = (
        f"Resumo dos dados carregados:\n"
        f"- Total de CVEs: {len(cves)}\n"
        f"- CVEs por ano: {years}\n"
        f"- Principais tipos de vulnerabilidades: {types}\n"
        f"- Distribuição de pontuação CVSS: {severities}\n"
    )

    prompt_input = (
        f"{examples}\n"
        f"{summary_input}\n"
        f"Com base nos dados acima, gere um resumo analítico das vulnerabilidades.\n"
        f"Output:"
    )

    response = model.generate_text(prompt=prompt_input, guardrails=False)
    return response.strip()
