from datetime import datetime

def registrar_alerta(mensagem):
    hora = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
    alerta = f"{hora} {mensagem}"
    print(alerta)
    with open("log.txt", "a") as log:
        log.write(alerta + "\n")