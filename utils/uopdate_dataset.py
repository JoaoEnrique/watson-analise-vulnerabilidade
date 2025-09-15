import requests
import time
from datetime import datetime, timezone
import json

def update_dataset(min_date="2020-01-01T00:00:00.000Z"):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0/"
    start = 0
    all_cves = []

    headers = {
        "User-Agent": "watson-watchdog/1.0"
    }

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

    while True:
        params = {
            "resultsPerPage": 2000,
            "startIndex": start,
        }
 
        resp = requests.get(url, params=params, headers=headers)

        if resp.status_code == 429:
            print("Limite de requisições atingido. Aguardando 30 segundos...")
            time.sleep(30)
            continue

        if resp.status_code != 200:
            print(f"Erro na requisição: {resp.status_code} - {resp.text[:200]}")
            break

        try:
            data = resp.json()
        except Exception as e:
            print("Erro ao decodificar JSON:", e, resp.text[:200])
            break

        vulns = data.get("vulnerabilities", [])
        if not vulns:
            break

        all_cves.extend(vulns)
        start += 2000

        # Pequena pausa entre páginas para evitar 429
        time.sleep(1)

    with open("cve_dataset.json", "w", encoding="utf-8") as f:
        json.dump({"vulnerabilities": all_cves}, f, ensure_ascii=False, indent=2)

    print(f"Dataset atualizado com {len(all_cves)} CVEs")