from datetime import datetime


def validar_texto(texto):
    if texto == "":
        return "Informe o texto da tarefa"
    if len(texto) > 100:
        return "O texto deve ter no máximo 100 caracteres"
    return ""


def validar_data(data):
    if len(data) != 10:
        return "Data inválida. Use DD/MM/AAAA"
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return "Data inválida. Use DD/MM/AAAA"
    return ""


def validar_hora(hora):
    mensagem = "Hora inválida. Use HH:MM entre 00:00 e 23:59"
    if len(hora) != 5 or hora[2] != ":":
        return mensagem
    horas = hora[:2]
    minutos = hora[3:]
    if not horas.isdigit() or not minutos.isdigit():
        return mensagem
    if int(horas) > 23 or int(minutos) > 59:
        return mensagem
    return ""