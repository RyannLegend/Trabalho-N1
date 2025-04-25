import sys
import os
from monitor import monitorar_diretorio

def menu():
    if len(sys.argv) < 2:
        print("Uso: python src/main.py <diretório> [intervalo_segundos]")
        sys.exit(1)

    pasta = sys.argv[1]
    intervalo = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    if not os.path.isdir(pasta):
        print(f"Erro: o caminho '{pasta}' não é um diretório válido.")
        sys.exit(2)

    monitorar_diretorio(pasta, intervalo=intervalo)

if __name__ == "__main__":
    menu()