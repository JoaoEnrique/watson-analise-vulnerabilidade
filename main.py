from utils.process import calculate_statistics, generate_watson_summary, parse_cve_file, save_upload
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("")
def home():
    return JSONResponse("Ola Mundo")

@app.post("/api/process")
async def process_file(file_input: UploadFile = File(...)):
    try:
        file_path = await save_upload(file_input)
        cves = parse_cve_file(file_path)
        years, types, severities = calculate_statistics(cves)
        summary = generate_watson_summary(cves)
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": f"Erro inesperado: {e}"}, status_code=500)

    return JSONResponse({
        "years": years,
        "types": types,
        "severities": severities,
        "watsonx_summary": summary
    })
