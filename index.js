import fs from "fs";
import path from "path";
import dotenv from "dotenv";
import axios from "axios";
import FormData from "form-data";

dotenv.config();

const API_URL = process.env.API_URL ?? "https://watson.pacoca.net/api";

export async function checkVulnerabilities() {
  try {
    const lockPath = path.resolve(process.cwd(), "package-lock.json");
    if (!fs.existsSync(lockPath)) throw new Error("package-lock.json não encontrado");

    const formData = new FormData();
    const fileStream = fs.createReadStream(lockPath);
    formData.append("file_input", fileStream, "package-lock.json");
    formData.append("api_key", process.env.API_KEY);
    formData.append("project_id", process.env.PROJECT_ID);

    const headers = formData.getHeaders();

    const response = await axios.post(`${API_URL}/process`, formData, {
        headers,
        maxBodyLength: Infinity
    });

    return response.data;
  } catch (err) {
    console.error("Erro ao verificar vulnerabilidades:", err);
    throw err;
  }
}
