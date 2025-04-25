import hashlib
import os

def calcular_hash(caminho_arquivo):
    sha256 = hashlib.sha256()
    try:
        with open(caminho_arquivo, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (PermissionError, FileNotFoundError):
        return None

def carregar_hashes_existentes(arquivo_hashes):
    if not os.path.exists(arquivo_hashes):
        return {}
    with open(arquivo_hashes, "r") as f:
        linhas = f.readlines()
    return dict(linha.strip().split("  ") for linha in linhas if "  " in linha)

def salvar_hashes(arquivo_hashes, dicionario):
    with open(arquivo_hashes, "w") as f:
        for caminho, hash_valor in dicionario.items():
            f.write(f"{caminho}  {hash_valor}\n")