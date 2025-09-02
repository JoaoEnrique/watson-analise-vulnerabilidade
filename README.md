# CVE Validator com Watson IA

Este sistema utiliza Watson IA para validar arquivos JSON de vulnerabilidades (CVE) e gerar relatórios inteligentes, facilitando a análise de riscos e mitigação de ameaças de segurança cibernética.

<img width="958" height="317" alt="image" src="https://github.com/user-attachments/assets/13825472-c165-4848-aac4-b87ee918bb7f" />
<img width="960" height="438" alt="image" src="https://github.com/user-attachments/assets/b96b40ae-ecb2-4e82-8db3-111c0a50a375" />

## Funcionalidades

✅ Validação Inteligente de CVEs
Processa e valida arquivos JSON contendo informações sobre vulnerabilidades conhecidas (Common Vulnerabilities and Exposures).

🧠 Análise com Watson IA
Integração com IBM Watson para analisar contexto, gravidade, impacto e possíveis soluções com base nos dados fornecidos.

📊 Geração de Relatórios Automatizados
Cria relatórios detalhados e compreensíveis, prontos para uso em auditorias, equipes de segurança e stakeholders.

📁 Entrada Esperada

O sistema espera um arquivo JSON no formato CVE, contendo dados como:

```json
{
  "cve_id": "CVE-2023-1234",
  "description": "Descrição da vulnerabilidade...",
  "impact": {
    "severity": "high"
  },
  "references": [...]
}
```
🔧 Tecnologias Utilizadas

IBM Watson X

Python

Reac JS

## 📦 Como Usar
Baixe o arquivo de CVE e envie para o Watson no frontend
```
https://github.com/JoaoEnrique/watson-analise-vulnerabilidade/blob/frontend/nvdcve-2.0-modified.json
```

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
