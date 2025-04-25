import os
import time
from verificador import calcular_hash, carregar_hashes_existentes, salvar_hashes
from alerta import registrar_alerta

def monitorar_diretorio(pasta, arquivo_hashes="hashes.txt", intervalo=10):
    print(f"Iniciando monitoramento de: {pasta}")
    hashes_anteriores = carregar_hashes_existentes(arquivo_hashes)

    while True:
        hashes_atuais = {}
        for root, _, arquivos in os.walk(pasta):
            for nome in arquivos:
                caminho = os.path.join(root, nome)
                hash_atual = calcular_hash(caminho)
                if hash_atual is None:
                    continue
                hashes_atuais[caminho] = hash_atual

                if caminho not in hashes_anteriores:
                    registrar_alerta(f"[NOVO] Arquivo detectado: {caminho}")
                elif hash_atual != hashes_anteriores[caminho]:
                    registrar_alerta(f"[ALTERADO] {caminho}")

        for antigo in hashes_anteriores:
            if antigo not in hashes_atuais:
                registrar_alerta(f"[REMOVIDO] {antigo}")

        salvar_hashes(arquivo_hashes, hashes_atuais)
        hashes_anteriores = hashes_atuais.copy()
        time.sleep(intervalo)