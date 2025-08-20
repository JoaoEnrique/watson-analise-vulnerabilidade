import os
import json
import csv
import pandas as pd
# from docx import Document

def parse_file(file_path: str) -> str:
    """
    Converte arquivos de diferentes formatos em texto.
    Suporta: .txt, .docx, .json, .csv, .xlsx, arquivos de código (.py, .java, .js, etc)
    """
    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".txt":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        elif ext == ".json":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                data = json.load(f)
                return json.dumps(data, indent=2, ensure_ascii=False)

        elif ext == ".csv":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                reader = csv.reader(f)
                return "\n".join([", ".join(row) for row in reader])

        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(file_path)
            return df.to_string(index=False)

        elif ext in [".py", ".java", ".js", ".ts", ".html", ".css", ".c", ".cpp", ".sql"]:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        else:
            return f"[AVISO] Tipo de arquivo {ext} não suportado ainda."

    except Exception as e:
        return f"[ERRO] Falha ao ler {file_path}: {e}"