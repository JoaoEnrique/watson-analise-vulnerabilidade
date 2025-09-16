# Watson Watchdog Backend
Recebe um arquivo package-lock e verifique se há vulnerabilidades

### Exemplo de saída:
```json
{
    "watson_summary": "- `form-data@^4.0.4` apresenta várias vulnerabilidades:\n  - CVE-2025-30153: Vulnerabilidade de negação de serviço (DoS) devido a uma falha de decodificação de ZIP bomb. Atualize para 0.131.0 ou superior.\n  - CVE-2025-47935: Vulnerabilidade de negação de serviço (DoS) devido a uma falha de manuseio de streams. Atualize para 2.0.0 ou superior.\n  - CVE-2025-47944: Vulnerabilidade de negação de serviço (DoS) devido a uma falha de manuseio de campos de upload vazios. Atualize para 2.0.1 ou superior"
    "vulnerable_dependencies": [
        {
            "package": "form-data",
            "version": "^4.0.4",
            "cve_id": "CVE-2025-30153",
            "description": "kin-openapi is a Go project for handling OpenAPI files. Prior to 0.131.0, when validating a request with a multipart/form-data schema, if the OpenAPI schema allows it, an attacker can upload a crafted ZIP file (e.g., a ZIP bomb), causing the server to consume all available system memory. The root cause comes from the ZipFileBodyDecoder, which is registered automatically by the module (contrary to what the documentation says). This vulnerability is fixed in 0.131.0."
        },
        {
            "package": "form-data",
            "version": "^4.0.4",
            "cve_id": "CVE-2025-47935",
            "description": "Multer is a node.js middleware for handling `multipart/form-data`. Versions prior to 2.0.0 are vulnerable to a resource exhaustion and memory leak issue due to improper stream handling. When the HTTP request stream emits an error, the internal `busboy` stream is not closed, violating Node.js stream safety guidance. This leads to unclosed streams accumulating over time, consuming memory and file descriptors. Under sustained or repeated failure conditions, this can result in denial of service, requiring manual server restarts to recover. All users of Multer handling file uploads are potentially impacted. Users should upgrade to 2.0.0 to receive a patch. No known workarounds are available."
        },
        {
            "package": "form-data",
            "version": "^4.0.4",
            "cve_id": "CVE-2025-47944",
            "description": "Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability that is present starting in version 1.4.4-lts.1 and prior to version 2.0.0 allows an attacker to trigger a Denial of Service (DoS) by sending a malformed multi-part upload request. This request causes an unhandled exception, leading to a crash of the process. Users should upgrade to version 2.0.0 to receive a patch. No known workarounds are available."
        },
        {
            "package": "form-data",
            "version": "^4.0.4",
            "cve_id": "CVE-2025-48997",
            "description": "Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability that is present starting in version 1.4.4-lts.1 and prior to version 2.0.1 allows an attacker to trigger a Denial of Service (DoS) by sending an upload file request with an empty string field name. This request causes an unhandled exception, leading to a crash of the process. Users should upgrade to `2.0.1` to receive a patch. No known workarounds are available."
        },
        {
            "package": "form-data",
            "version": "^4.0.4",
            "cve_id": "CVE-2025-7338",
            "description": "Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability that is present starting in version 1.4.4-lts.1 and prior to version 2.0.2 allows an attacker to trigger a Denial of Service (DoS) by sending a malformed multi-part upload request. This request causes an unhandled exception, leading to a crash of the process. Users should upgrade to version 2.0.2 to receive a patch. No known workarounds are available."
        }
    ],
}

```
