# Watson Watchdog

**`watson-watchdog`** é uma ferramenta que usa **inteligência artificial** para verificar vulnerabilidades em dependências de projetos Node.js, analisando o `package-lock.json`. Ideal para integração em **CI/CD pipelines**.


## 🚀 Funcionalidades

- Backend: https://github.com/JoaoEnrique/watson-watchdog/tree/backend
- Analisa dependências do `package-lock.json` em busca de CVEs.  
- Integra com um **servidor FastAPI** que consulta um banco SQLite com CVEs.  
- Gera um resumo usando **IA** para explicar as vulnerabilidades.  
- Pode ser usado em **CLI**, scripts Node.js ou pipelines CI/CD.  
- Exit code 1 em caso de vulnerabilidades, permitindo falhar builds automaticamente.


## 📦 Instalação

### Instalação local

```bash
npm install --save-dev watson-watchdog
```

## 🌐 Requisitos
É necessário obter uma conta no Watsson Studio com créditos para utilizar o Watson e adicionar a chave de API e id do projeto no .env

```bash
API_URL=http://127.0.0.1:8000/api #para rodar back local (opcional)
API_KEY=
PROJECT_ID=
```


## Usando npx
Execute o comando para fazer a analise local das vulnerabilidades do seu projeto.
```bash
npx watson-watchdog
```


## ⚡ CLI

Após instalar, você pode rodar diretamente no terminal:

watson-watchdog


### Exemplo de saída:

```
❌ Vulnerabilidades encontradas!
┌─────────┬───────────┬────────┬───────────┬─────────────────────────────┐
│ (index) │ Pacote    │ Versão │ CVE       │ Descrição                   │
├─────────┼───────────┼────────┼───────────┼─────────────────────────────┤
│ 0       │ express   │ 4.17.1 │ CVE-XXXX  │ Description of vulnerability│
└─────────┴───────────┴────────┴───────────┴─────────────────────────────┘
```
<img width="1531" height="807" alt="image" src="https://github.com/user-attachments/assets/31f87c08-2092-4e4e-bdd9-cc6747a0e60e" />



O comando retorna exit code 1 se houver vulnerabilidades.

## 📖 Uso em Node.js

Você também pode usar como módulo:

```js
import { checkVulnerabilities } from "watson-watchdog";

(async () => {
  const result = await checkVulnerabilities();
  console.log(result);
})();


Retorno:

{
  "vulnerable_dependencies": [
    {
      "package": "express",
      "version": "4.17.1",
      "cve_id": "CVE-XXXX",
      "description": "Descrição da vulnerabilidade..."
    }
  ],
  "watson_summary": "Resumo gerado pela IA..."
}
```

## 🔧 Integração com GitHub Actions
```yml
name: Security Check

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - run: npm install

      - name: Run Vulnerability Check
        run: npx watson-watchdog
        env:
          # vars em secrets no git
          API_URL: ${{ secrets.API_URL }} #para rodar back local (opcional)
          API_KEY: ${{ secrets.API_KEY }}
          PROJECT_ID: ${{ secrets.PROJECT_ID }}
```

Se houver vulnerabilidades, o job falha automaticamente.


## 📜 Licença

MIT License – sinta-se livre para usar e modificar.
