import os
# from flask import Flask, request, jsonify
from parser_utils import parse_file
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from collections import Counter, defaultdict
from fastapi.responses import JSONResponse
import json

load_dotenv()

# app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Configurações da AI ----
api_key = os.getenv("API_KEY")
project_id = os.getenv("PROJ_ID")
space_id = os.getenv("SPACE_ID")

credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
    api_key=api_key
)

model_id = "ibm/granite-3-8b-instruct"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 200,
    "min_new_tokens": 0,
    "repetition_penalty": 1
}

model = ModelInference(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id,
    space_id=space_id
)

# ---- Exemplos fixos do prompt ----
EXAMPLES = """Você é um assistente de análise de dados em segurança da informação. 
Sua tarefa é ajudar a explorar dados de vulnerabilidades CVE (NVD), 
mostrando tendências por ano, tipos de falha e severidade (pontuação CVSS).

Input: Mostre os tipos de vulnerabilidades mais comuns em 2022.

Output: As vulnerabilidades mais comuns em 2022 foram:
1. Cross-Site Scripting (XSS)
2. Buffer Overflow
3. Injeção de código
Esses tipos de falha aparecem com maior frequência no dataset NVD para o ano de 2022.

Input: Liste a quantidade de CVEs por ano de 2020 até 2023.
Output: Quantidade de CVEs por ano:
- 2020: 18.362
- 2021: 20.142
- 2022: 25.032
- 2023: 26.051

Input: Mostre a distribuição de pontuações CVSS em 2021.
Output:"""

# ---- Rota front-end ----
@app.route("/")
def index():
    return app.send_static_file("index.html")

# ---- Rota API para processar entrada ----
# @app.route("/process", methods=["POST"])
# def process_input():
#     text_input = request.form.get("text_input", "")
#     file = request.files.get("file_input")

#     if file:
#         file_path = os.path.join("uploads", file.filename)
#         os.makedirs("uploads", exist_ok=True)
#         file.save(file_path)
#         text_input = parse_file(file_path)

#     # Combina exemplos fixos + input do usuário
#     prompt_input = f"{EXAMPLES}\nEntrada: {text_input}\nSaída:"

#     # Chamada ao modelo IBM Watsonx
#     generated_response = model.generate_text(prompt=prompt_input, guardrails=False)

#     # ---- FILTRO: corta tudo após a palavra 'Entrada' ----
#     filtered_response = generated_response.split("Entrada")[0].strip()

#     return jsonify({"result": filtered_response})

@app.post("/process")
async def process_file(file_input: UploadFile = File(...)):
    """Recebe arquivo CVE JSON e retorna estatísticas"""
    file_path = os.path.join("uploads", file_input.filename)
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(await file_input.read())

    data = parse_file(file_path)  # parseia JSON em texto/objeto

    # ---- Parser para novo formato NVD ----
    try:
        cves = json.loads(data)["vulnerabilities"]
    except KeyError as e:
        return JSONResponse({"error": f"Chave faltando no arquivo: {e}"}, status_code=400)
    except json.JSONDecodeError as e:
        return JSONResponse({"error": f"Erro ao decodificar JSON: {e}"}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": f"Erro inesperado: {e}"}, status_code=500)

    # Extração
    anos = Counter()
    tipos = Counter()
    severidades = Counter()

    for item in cves:
        cve_data = item.get("cve", {})

        # ano = data_publicacao
        ano = cve_data.get("published", "0000")[:4]
        anos[ano] += 1

        # tipo de falha (CWE)
        weaknesses = cve_data.get("weaknesses", [])
        if weaknesses and "description" in weaknesses[0]:
            cwe_desc = weaknesses[0]["description"]
            if cwe_desc:
                tipos[cwe_desc[0].get("value", "Unknown")] += 1

        # severidade CVSS
        metrics = cve_data.get("metrics", {})
        if "cvssMetricV31" in metrics and metrics["cvssMetricV31"]:
            score = metrics["cvssMetricV31"][0]["cvssData"].get("baseScore")
            if score is not None:
                severidades[str(score)] += 1
        elif "cvssMetricV2" in metrics and metrics["cvssMetricV2"]:
            score = metrics["cvssMetricV2"][0]["cvssData"].get("baseScore")
            if score is not None:
                severidades[str(score)] += 1

    # Estrutura para frontend
    response = {
        "anos": dict(anos),
        "tipos": dict(tipos.most_common(10)),
        "severidades": dict(severidades),
    }

    return JSONResponse(response)

if __name__ == "__main__":
    app.run(debug=True)