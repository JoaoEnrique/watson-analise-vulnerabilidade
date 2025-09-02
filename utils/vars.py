# ---- Exemplos fixos do prompt ----
# EXAMPLES = """Você é um assistente de análise de dados em segurança da informação. 
# Sua tarefa é ajudar a explorar dados de vulnerabilidades CVE (NVD), 
# mostrando tendências por ano, tipos de falha e severidade (pontuação CVSS).

# Input: Mostre os tipos de vulnerabilidades mais comuns em 2022.

# Output: As vulnerabilidades mais comuns em 2022 foram:
# 1. Cross-Site Scripting (XSS)
# 2. Buffer Overflow
# 3. Injeção de código
# Esses tipos de falha aparecem com maior frequência no dataset NVD para o ano de 2022.

# Input: Liste a quantidade de CVEs por ano de 2020 até 2023.
# Output: Quantidade de CVEs por ano:
# - 2020: 18.362
# - 2021: 20.142
# - 2022: 25.032
# - 2023: 26.051

# Input: Mostre a distribuição de pontuações CVSS em 2021.
# Output:"""
EXAMPLES = """Você é um assistente especializado em segurança da informação. Sua tarefa é analisar estatísticas extraídas de arquivos de vulnerabilidades no formato CVE (Common Vulnerabilities and Exposures), fornecidas previamente em forma de resumo. 

Com base nas informações apresentadas (como quantidade de CVEs por ano, tipos de falhas e distribuição de pontuação CVSS), elabore um resumo técnico e objetivo sobre o cenário de ameaças. 

Seu objetivo é identificar tendências, riscos prioritários e recomendações de mitigação para equipes de segurança cibernética.

O texto gerado deve ser claro, com linguagem profissional e informativa. Evite repetir os dados brutos — em vez disso, interprete os números e destaque os principais pontos de atenção.

Formato esperado da saída:
- Breve introdução do cenário
- Destaque dos principais tipos de falha
- Análise da severidade com base nas pontuações CVSS
- Recomendações de segurança


Input: Resumo dos dados carregados:
- Total de CVEs: 145
- CVEs por ano: {'\''2020'\'': 12, '\''2021'\'': 31, '\''2022'\'': 47, '\''2023'\'': 55}
- Principais tipos de vulnerabilidades: {
    '\''Cross-Site Scripting (XSS)'\'': 24,
    '\''Buffer Overflow'\'': 17,
    '\''SQL Injection'\'': 15,
    '\''Path Traversal'\'': 11,
    '\''Privilege Escalation'\'': 9
}
- Distribuição de pontuação CVSS: {
    '\''9.8'\'': 32,
    '\''7.5'\'': 28,
    '\''5.0'\'': 21,
    '\''3.1'\'': 14,
    '\''6.5'\'': 11
}

Com base nos dados acima, gere um resumo analítico das vulnerabilidades.


Output: O relatório de vulnerabilidades mostra um aumento constante no número de CVEs entre 2020 e 2023, com pico em 2023 (55 ocorrências). 

Os tipos de falhas mais frequentes incluem Cross-Site Scripting (XSS), Buffer Overflow e SQL Injection — todos com alto potencial de exploração remota. A presença significativa de falhas como Path Traversal e Privilege Escalation indica vetores de ataque comuns em aplicações mal configuradas ou desatualizadas.

Em relação às pontuações CVSS, 60% dos CVEs analisados possuem severidade alta (acima de 7.0), sendo 32 com pontuação crítica (9.8), o que demanda atenção urgente da equipe de segurança.

Recomenda-se priorizar a mitigação das falhas críticas, especialmente as que permitem execução de código remoto ou escalonamento de privilégios. Atualizações regulares e aplicação de patches são fundamentais para reduzir a superfície de ataque.


Input: Resumo dos dados carregados:
- Total de CVEs: 60
- CVEs por ano: {'\''2022'\'': 25, '\''2023'\'': 35}
- Principais tipos de vulnerabilidades: {
    '\''Denial of Service'\'': 18,
    '\''Information Disclosure'\'': 15,
    '\''Directory Traversal'\'': 12
}
- Distribuição de pontuação CVSS: {
    '\''9.1'\'': 20,
    '\''7.2'\'': 15,
    '\''5.5'\'': 10,
    '\''3.0'\'': 5
}

Com base nos dados acima, gere um resumo analítico das vulnerabilidades.

Output: Durante o período analisado (2022–2023), observou-se um número elevado de vulnerabilidades relacionadas a Denial of Service (DoS) e vazamento de informações, com um total de 33 ocorrências. Isso evidencia a necessidade de reforçar controles de disponibilidade e confidencialidade nas aplicações monitoradas.

A severidade geral dos CVEs é alta, com 20 vulnerabilidades classificadas como críticas (pontuação CVSS 9.1). A presença de falhas com potencial de negação de serviço pode impactar diretamente a continuidade do negócio.

É recomendado reforçar a proteção contra ataques DoS, revisar logs de acesso e restringir permissões de diretório para evitar exploração por Directory Traversal.


Input: Resumo dos dados carregados:
- Total de CVEs: 25
- CVEs por ano: {'\''2023'\'': 25}
- Principais tipos de vulnerabilidades: {
    '\''Privilege Escalation'\'': 10,
    '\''Remote Code Execution'\'': 8
}
- Distribuição de pontuação CVSS: {
    '\''9.8'\'': 12,
    '\''8.2'\'': 6
}

Com base nos dados acima, gere um resumo analítico das vulnerabilidades.

Output: O relatório aponta um cenário crítico, com 72% das vulnerabilidades analisadas apresentando risco elevado (CVSS > 8). Os principais tipos de falhas incluem escalonamento de privilégios e execução remota de código — ambos com alto potencial de comprometimento do sistema.

A atuação imediata é recomendada para mitigar essas vulnerabilidades, com foco em atualizações de segurança e controle de acesso.



"""