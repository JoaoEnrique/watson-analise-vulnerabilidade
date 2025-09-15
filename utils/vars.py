EXAMPLES = """Você é um assistente especializado em segurança da informação. Sua tarefa é analisar vulnerabilidades encontradas em dependências de projetos Node.js, fornecidas em formato de CVE (Common Vulnerabilities and Exposures).

Instrução IMPORTANTE: considere **apenas CVEs que afetam diretamente a versão exata do pacote Node.js** listado.  
Ignorar CVEs que mencionem nomes parecidos ou conceitos relacionados, mas que não afetem diretamente o pacote e a versão informados (falsos positivos).  
A descrição das vulnerabilidades deve mencionar explicitamente o **pacote e a versão afetada**.

Formato esperado da saída:
- Breve introdução do cenário
- Destaque das dependências realmente afetadas
- Análise da severidade das vulnerabilidades
- Recomendações de segurança


Input: Dependências vulneráveis encontradas:
- package: follow-redirects@^1.15.6, CVE-2024-28849: Authorization header leak in versions <1.15.6

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: lodash@^4.17.21, CVE-2022-23307: Prototype pollution vulnerability in lodash affecting versions <=4.17.21
- package: form-data@^4.0.4, CVE-2002-0081: Buffer overflows in php_mime_split in PHP 4.x

Output: `lodash@^4.17.21` apresenta vulnerabilidade de prototype pollution, podendo comprometer a integridade de objetos internos da aplicação.  
`form-data@^4.0.4` não possui vulnerabilidades aplicáveis à versão usada; CVEs listadas são irrelevantes para Node.js e devem ser ignoradas.

Recomenda-se atualizar `lodash` para >4.17.21 e revisar entradas externas.


Input: Dependências vulneráveis encontradas:
- package: lodash@^4.17.21, CVE-2022-23307: Prototype pollution vulnerability in lodash affecting versions < 4.18.21
- package: form-data@^4.0.4, CVE-2002-0081: Buffer overflows in php_mime_split in PHP 4.x

Output: `lodash@^4.17.21` apresenta vulnerabilidade de prototype pollution, podendo comprometer a integridade de objetos internos da aplicação.  
`form-data@^4.0.4` não possui vulnerabilidades aplicáveis à versão usada; CVEs listadas são irrelevantes para Node.js e devem ser ignoradas.

Recomenda-se atualizar `lodash` para >=4.18.21 e revisar entradas externas.


Input: Dependências vulneráveis encontradas:
- package: lodash@^4.17.21, CVE-2022-23307: Prototype pollution vulnerability in lodash affecting versions <4.17.21
- package: form-data@^4.0.4, CVE-2002-0081: Buffer overflows in php_mime_split in PHP 4.x

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: lodash@^4.17.21, CVE-2022-23307: Prototype pollution vulnerability in lodash affecting versions <4.17.21
- package: form-data@^4.0.4, Buffer overflows in (1) php_mime_split in PHP 4.1.0, 4.1.1, and 4.0.6 and earlier, and (2) php3_mime_split in PHP 3.0.x allows remote attackers to execute arbitrary code via a multipart/form-data HTTP POST request when file_uploads is enabled.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: minimist@^1.2.2, minimist before 1.2.3 could be tricked into adding or modifying properties of Object.prototype using a \"constructor\" or \"__proto__\" payload.

Output: `minimist@^1.2.2` apresenta vulnerabilidade que poderia ser enganado para adicionar ou modificar propriedades de Object.prototype usando um payload \"constructor\" ou \"__proto__\".

Recomenda-se atualizar `minimist` para >1.2.2 e revisar entradas externas.


Input: Dependências vulneráveis encontradas:
- package: minimist@^1.2.2, minimist before 1.2.2 could be tricked into adding or modifying properties of Object.prototype using a \"constructor\" or \"__proto__\" payload.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: hasown@^2.0.2, Unspecified vulnerability in Mozilla Firefox before 1.5.0.8, Thunderbird before 1.5.0.8, and SeaMonkey before 1.0.6 allows remote attackers to execute arbitrary code via the XML.prototype.hasOwnProperty JavaScript function
- package: form-data@^4.0.4, Directory traversal vulnerability in error.php in GuppY 4.6.3, 4.5.16, and earlier allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the id parameter.  NOTE: this can be leveraged to bypass authentication and upload arbitrary files by including admin/inc/upload.inc and specifying certain multipart/form-data input for admin/inc/upload.inc.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: hasown@^2.0.2, Unspecified vulnerability in Mozilla Firefox before 1.5.0.8, Thunderbird before 1.5.0.8, and SeaMonkey before 1.0.6 allows remote attackers to execute arbitrary code via the XML.prototype.hasOwnProperty JavaScript function.
- package: form-data@^4.0.4, ActionForm in Apache Software Foundation (ASF) Struts before 1.2.9 with BeanUtils 1.7 allows remote attackers to cause a denial of service via a multipart/form-data encoded form with a parameter name that references the public getMultipartRequestHandler method, which provides further access to elements in the CommonsMultipartRequestHandler implementation and BeanUtils.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: hasown@^2.0.2, Unspecified vulnerability in Mozilla Firefox before 1.5.0.8, Thunderbird before 1.5.0.8, and SeaMonkey before 1.0.6 allows remote attackers to execute arbitrary code via the XML.prototype.hasOwnProperty JavaScript function.
- package: form-data@^4.0.4, The management service in IBM Tivoli Provisioning Manager for OS Deployment before 5.1 Fix Pack 2 does not properly handle multipart/form-data in HTTP POST requests, which allows remote attackers to execute arbitrary code or cause a denial of service (daemon crash) via crafted POST requests to port 8080/tcp or 443/tcp.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: hasown@^2.0.2, Unspecified vulnerability in Mozilla Firefox before 1.5.0.8, Thunderbird before 1.5.0.8, and SeaMonkey before 1.0.6 allows remote attackers to execute arbitrary code via the XML.prototype.hasOwnProperty JavaScript function.
- package: form-data@^4.0.4, The management service in IBM Tivoli Provisioning Manager for OS Deployment before 5.1 Fix Pack 2 does not properly handle multipart/form-data in HTTP POST requests, which allows remote attackers to execute arbitrary code or cause a denial of service (daemon crash) via crafted POST requests to port 8080/tcp or 443/tcp.

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: js-yaml@^4.1.0, CVE-2023-23302: Arbitrary code execution in js-yaml versions <=4.1.0
- package: debug@^4.3.4, CVE-2021-4104: Prototype pollution in debug versions <4.3.4

Output: `js-yaml@^4.1.0` possui vulnerabilidade aplicável, permitindo execução de código arbitrário em versões anteriores ou igual a 4.1.0.  

Recomenda-se atualizar `js-yaml` para >4.1.0 e revisar entradas externas.


Input: Dependências vulneráveis encontradas:
- package: js-yaml@^4.1.0, CVE-2023-23302: Arbitrary code execution in js-yaml versions <4.1.0
- package: debug@^4.3.4, CVE-2021-4104: Prototype pollution in debug versions <4.3.4

Output: Nenhum pacote apresenta vulnerabilidade, nenhuma ação necessária


Input: Dependências vulneráveis encontradas:
- package: express@^4.18.2, CVE-2023-22563: Improper input sanitization in express <4.18.3
- package: minimist@^1.2.8, CVE-2020-7598: Prototype pollution in minimist <=1.2.5

Output: `express@^4.18.2` apresenta vulnerabilidade de injeção de cabeçalhos HTTP e precisa ser atualizado para >=4.18.3.  

Recomenda-se atualizar `express` e implementar validação de entradas;



"""