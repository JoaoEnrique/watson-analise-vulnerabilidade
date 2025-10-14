def extract_packages(package_lock_data):
    """
    Extrai apenas as dependências diretas do projeto,
    que ficam dentro de "packages": { "": { "dependencies": { ... } } }.
    Retorna uma lista de (nome, versão).
    """
    root_pkg = package_lock_data.get("", {})
    dependencies = root_pkg.get("dependencies", {})
    all_packages = []

    for name, version in dependencies.items():
        all_packages.append((name, version))

    print("package_lock_data")
    print(package_lock_data)
    print("all_packages")
    print(all_packages)
    return all_packages


def extract_all_packages(packages_dict):
    """
    Retorna lista completa de pacotes (nome, versão) de qualquer nível no package-lock v3.
    """
    all_packages = []

    def recurse(pkg_info, parent_name=None):
        # Tenta pegar o nome do pacote
        name = pkg_info.get("name", parent_name)
        version = pkg_info.get("version")
        if name and version:
            all_packages.append((name, version))
        
        # Processa sub-dependencies
        for sub_name, sub_version in pkg_info.get("dependencies", {}).items():
            # O sub_name aqui é a chave do dicionário, mas precisamos passar a versão também
            # Cria um "mock" de pacote com nome/sub_version, já que package-lock v3 não dá info completa
            sub_pkg_info = {"name": sub_name, "version": sub_version}
            recurse(sub_pkg_info, parent_name=sub_name)

    for pkg_path, pkg_info in packages_dict.items():
        if pkg_path == "":
            continue
        recurse(pkg_info)

    # Remove duplicados
    return list(set(all_packages))


import sqlite3

def extract_all_packages(packages_dict):
    all_packages = []

    def recurse(pkg_info, parent_name=None):
        name = pkg_info.get("name", parent_name)
        version = pkg_info.get("version")
        if name and version:
            all_packages.append((name, version))

        for sub_name, sub_version in pkg_info.get("dependencies", {}).items():
            sub_pkg_info = {"name": sub_name, "version": sub_version}
            recurse(sub_pkg_info, parent_name=sub_name)

    for pkg_path, pkg_info in packages_dict.items():
        if pkg_path == "":
            continue
        recurse(pkg_info)

    return list(set(all_packages))


# def intersect_dependencies(lock_data, db_path):
#     """
#     Verifica dependências do package-lock.json contra CVEs armazenados no SQLite.
#     """
#     packages_dict = lock_data.get("packages", {})
#     all_packages = extract_all_packages(packages_dict)

#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()

#     vulnerable_packages = []

#     for name, version in all_packages:
#         # Busca por nome do pacote nas descrições
#         cur.execute("SELECT id, description FROM cves WHERE description LIKE ?", (f"%{name}%",))
#         for row in cur.fetchall():
#             cve_id, description = row
#             if "node" in description.lower() or "module" in description.lower():
#                 vulnerable_packages.append({
#                     "package": name,
#                     "version": version,
#                     "cve_id": cve_id,
#                     "description": description
#                 })


#     conn.close()
#     return vulnerable_packages

def intersect_dependencies(lock_data, db_path, include_subdependencies=False):
    """
    Verifica dependências do package-lock.json contra CVEs armazenados no SQLite.
    Se include_subdependencies=True, analisa também dependências de dependências.
    """
    packages_dict = lock_data.get("packages", {})

    if include_subdependencies:
        all_packages = extract_all_packages(packages_dict)
    else:
        all_packages = extract_packages(packages_dict)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    vulnerable_packages = []

    for name, version in all_packages:
        cur.execute("SELECT id, description FROM cves WHERE description LIKE ?", (f"%{name}%",))
        for row in cur.fetchall():
            cve_id, description = row
            if "node" in description.lower() or "module" in description.lower():
                vulnerable_packages.append({
                    "package": name,
                    "version": version,
                    "cve_id": cve_id,
                    "description": description
                })

    conn.close()
    return vulnerable_packages


