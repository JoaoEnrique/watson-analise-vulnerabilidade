from utils.process import intersect_dependencies
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.watson import model
from utils.vars import EXAMPLES
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return JSONResponse("Ola Mundo")

@app.post("/api/process")
async def process_file(file_input: UploadFile = File(...)):
    try:
        content = await file_input.read()
        lock_data = json.loads(content)

        # Busca direto no banco SQLite
        vulnerable_deps = intersect_dependencies(lock_data, "cve_dataset.db")

        if not vulnerable_deps:
            return JSONResponse({
                "message": "Nenhuma vulnerabilidade encontrada",
                "vulnerable_dependencies": []
            })

        # Prepara prompt para Watson
        prompt_input = "Dependências vulneráveis encontradas:\n"
        for dep in vulnerable_deps:
            prompt_input += f"- {dep['package']}@{dep['version']}: {dep['cve_id']} - {dep['description']}\n"

        prompt = f"{EXAMPLES}\n{prompt_input}\nOutput:"

        # watson_result = model.generate_text(prompt=prompt, guardrails=False)
        # summary = watson_result.strip()
        summary = "ioavsasas"

        return JSONResponse({
            "vulnerable_dependencies": vulnerable_deps,
            "watson_summary": summary
        })

    except json.JSONDecodeError:
        return JSONResponse({"error": "Arquivo inválido"}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": f"Erro inesperado: {str(e)}"}, status_code=500)