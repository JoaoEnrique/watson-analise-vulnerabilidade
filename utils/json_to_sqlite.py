import sqlite3
import ijson

DB_FILE = "cve_dataset.db"
JSON_FILE = "cve_dataset.json"

def create_database():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # Cria tabela
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cves (
            id TEXT PRIMARY KEY,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()

def import_json_to_sqlite():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        parser = ijson.items(f, "vulnerabilities.item")
        count = 0

        for vuln in parser:
            cve_id = vuln.get("cve", {}).get("id")
            descriptions = vuln.get("cve", {}).get("descriptions", [])
            
            # pega descrição em inglês se existir
            desc = ""
            for d in descriptions:
                if d.get("lang") == "en":
                    desc = d.get("value", "")
                    break

            if not desc and descriptions:
                desc = descriptions[0].get("value", "")

            if cve_id:
                cur.execute(
                    "INSERT OR IGNORE INTO cves (id, description) VALUES (?, ?)",
                    (cve_id, desc)
                )
                count += 1

            if count % 10000 == 0:
                conn.commit()
                print(f"{count} registros inseridos...")

    conn.commit()
    conn.close()
    print(f"Importação concluída! Total: {count} registros.")

if __name__ == "__main__":
    create_database()
    import_json_to_sqlite()
