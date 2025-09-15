#!/usr/bin/env node
import { checkVulnerabilities } from "./index.js";

(async () => {
  try {
    const result = await checkVulnerabilities();

    if (result.vulnerable_dependencies?.length) {
      console.error("❌ Vulnerabilidades encontradas!");
      console.error("Análise da IA:", result.watson_summary);
      console.table(result.vulnerable_dependencies.map(dep => ({
        Pacote: dep.package,
        Versão: dep.version,
        CVE: dep.cve_id,
        Descrição: dep.description.slice(0, 100) + "..."
      })));
      process.exit(1); // falha no CI/CD
    } else {
      console.log("✅ Nenhuma vulnerabilidade encontrada!");
      process.exit(0);
    }
  } catch (err) {
    console.error("Erro:", err.message);
    process.exit(1);
  }
})();
