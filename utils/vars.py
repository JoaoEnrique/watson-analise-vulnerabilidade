EXAMPLES = """Você é um assistente especializado em segurança da informação.
Sua tarefa é analisar vulnerabilidades encontradas em dependências de projetos Node.js (em formato CVE).

Instrução IMPORTANTE: considere **apenas CVEs que afetam diretamente a versão exata do pacote Node.js** listado.  
Ignorar CVEs que mencionem nomes parecidos ou conceitos relacionados, mas que não afetem diretamente o pacote e a versão informados (falsos positivos).  
A descrição das vulnerabilidades deve mencionar explicitamente o **pacote e a versão afetada**.

Regras:
- Analise apenas a lista fornecida no Input.
- No Output, explique de forma objetiva se a vulnerabilidade se aplica ou não.
- Forneça recomendações de atualização ou mitigação quando aplicável.
- NÃO repita nem copie o conteúdo do Input: no Output.
- O Output deve conter apenas a análise e a recomendação.


Input: Dependências vulneráveis encontradas:
- package: follow-redirects@^1.15.6, CVE-2024-28849: Authorization header leak in versions <1.15.6

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: lodash@^4.17.21, CVE-2022-23307: Prototype pollution vulnerability in lodash affecting versions <4.17.21
- package: form-data@^4.0.4, CVE-2002-0081: Buffer overflows in php_mime_split in PHP 4.x

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: express@^4.18.2, CVE-2023-22563: Improper input sanitization in express <4.18.3
- package: minimist@^1.2.8, CVE-2020-7598: Prototype pollution in minimist <=1.2.5

Output: `express@^4.18.2` apresenta vulnerabilidade de injeção de cabeçalhos HTTP (CVE-2023-22563) e precisa ser atualizado para >=4.18.3.  
Recomenda-se atualizar `express` e implementar validação de entradas


Input: Dependências vulneráveis encontradas:
- package: js-yaml@^4.1.0, CVE-2023-23302: Arbitrary code execution in js-yaml versions <4.1.0
- package: debug@^4.3.4, CVE-2021-4104: Prototype pollution in debug versions <4.3.4

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: js-yaml@^4.1.0, CVE-2023-23302: Arbitrary code execution in js-yaml versions <=4.1.0
- package: debug@^4.3.4, CVE-2021-4104: Prototype pollution in debug versions <4.3.4

Output: `js-yaml@^4.1.0` apresenta vulnerabilidade de execução arbitrária de código (CVE-2023-23302) e precisa ser atualizado para uma versão corrigida (>4.1.0).
Recomenda-se atualizar js-yaml e revisar pontos de desserialização de YAML.


Input: Dependências vulneráveis encontradas:
- package: js-yaml@^4.1.0, CVE-2023-23302: Arbitrary code execution in js-yaml versions <4.1.0
- package: debug@^4.3.4, CVE-2021-4104: Prototype pollution in debug versions <=4.3.4

Output: `debug@^4.3.4` apresenta vulnerabilidade de prototype pollution (CVE-2021-4104) e precisa ser atualizado para >=4.3.5.
Recomenda-se atualizar debug e implementar validação de objetos recebidos.


Input: Dependências vulneráveis encontradas:
- package: lodash@^4.18.21, CVE-2022-23307: Prototype pollution vulnerability in lodash affecting versions < 4.18.21
- package: form-data@^4.0.4, CVE-2002-0081: Buffer overflows in php_mime_split in PHP 4.x

Output:  `lodash@^4.18.21` apresenta vulnerabilidade de prototype pollution (CVE-2022-23307), podendo comprometer a integridade de objetos internos da aplicação.  
Recomenda-se atualizar `lodash` para >=4.18.21 e revisar entradas externas


Input: Dependências vulneráveis encontradas:
- package: js-yaml@^4.1.0, CVE-2023-23302: Arbitrary code execution in js-yaml versions <=4.1.0
- package: debug@^4.3.4, CVE-2021-4104: Prototype pollution in debug versions < 4.3.4

Output: `js-yaml@^4.1.0` apresenta vulnerabilidade de execução arbitrária de código (CVE-2023-23302) e precisa ser atualizado para uma versão corrigida (>4.1.0).
`debug@^4.3.4` apresenta vulnerabilidade de prototype pollution (CVE-2021-4104) e precisa ser atualizado para uma versão corrigida (>=4.3.4)
Recomenda-se atualizar js-yaml e revisar pontos de desserialização de YAML.


Input: Dependências vulneráveis encontradas:
- package: minimist@^0.2.1, CVE-2020-7598: Prototype pollution in minimist <0.2.1

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: axios@^0.21.0, CVE-2021-3749: SSRF vulnerability in axios <0.21.1
- package: tar@^6.1.5, CVE-2021-32804: Arbitrary file creation when extracting tarballs

Output:  `axios@^0.21.0` apresenta vulnerabilidade de SSRF (CVE-2021-3749) e precisa ser atualizado para >=0.21.1.
Recomenda-se atualizar axios e implementar validação de entradas.


Input: Dependências vulneráveis encontradas:
- package: ansi-regex@^5.0.0, CVE-2021-3807: Inefficient Regular Expression Complexity in ansi-regex <=5.0.0

Output: `ansi-regex@^5.0.0` apresenta vulnerabilidade Complexidade de Expressão Regular Ineficiente em ansi-regex (CVE-2021-3807) e precisa ser atualizado para > 5.0.0
Recomenda-se atualizar ansi-regex.


Input: Dependências vulneráveis encontradas:
- package: `form-data@^4.0.4`, kin-openapi is a Go project for handling OpenAPI files. Prior to 0.131.0, when validating a request with a multipart/form-data schema, if the OpenAPI schema allows it, an attacker can upload a crafted ZIP file (e.g., a ZIP bomb), causing the server to consume all available system memory. The root cause comes from the ZipFileBodyDecoder, which is registered automatically by the module (contrary to what the documentation says). This vulnerability is fixed in 0.131.0.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: - package: `mime-types@^2.1.12`TYPO3 is an open source PHP based web content management system. In TYPO3 before versions 8.7.40, 9.5.25, 10.4.14, 11.1.1 due to improper input validation, attackers can by-pass restrictions of predefined options and submit arbitrary data in the Form Designer backend module of the Form Framework. In the default configuration of the Form Framework this allows attackers to explicitly allow arbitrary mime-types for file uploads - however, default _fileDenyPattern_ successfully blocked files like _.htaccess_ or _malicious.php_. Besides that, attackers can persist those files in any writable directory of the corresponding TYPO3 installation. A valid backend user account with access to the form module is needed to exploit this vulnerability. This is fixed in versions 8.7.40, 9.5.25, 10.4.14, 11.1.1.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária

"""