from utils.process import intersect_dependencies
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.watson import getModel
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
async def process_file(
    file_input: UploadFile = File(...),
    api_key: str = Form(...),
    project_id: str = Form(...)
):
    try:
        model = getModel(api_key, project_id)
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

        prompt = f"{EXAMPLES}\nInput: {prompt_input}\nOutput:"

        print("prompt")
        print(prompt)
        watson_result = model.generate_text(prompt=prompt, guardrails=False)
        summary = watson_result.strip()

        # Filtra vulnerabilidades confirmadas pelo Watson
        vulnerable_deps_confirmed = [
            dep for dep in vulnerable_deps
            if dep["package"] in summary
        ]

        if not vulnerable_deps_confirmed:
            return JSONResponse({
                "message": "Nenhuma vulnerabilidade confirmada pelo Watson",
                "vulnerable_dependencies": []
            })

        # Retorna apenas os confirmados
        return JSONResponse({
            "vulnerable_dependencies": vulnerable_deps_confirmed,
            "watson_summary": summary
        })

        # return JSONResponse({
        #     "vulnerable_dependencies": vulnerable_deps,
        #     "watson_summary": summary
        # })

    except json.JSONDecodeError:
        return JSONResponse({"error": "Arquivo inválido"}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": f"Erro inesperado: {str(e)}"}, status_code=500)