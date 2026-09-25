import json
import os
from datetime import datetime

PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados")
ARQUIVO = os.path.join(PASTA, "tarefas.json")


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return [], ""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
    except (OSError, ValueError) as erro:
        print("Erro ao ler o arquivo:", erro)
        return [], "Não foi possível ler o arquivo de tarefas: " + str(erro)
    if type(tarefas) != list:
        return [], "O arquivo de tarefas está em formato inesperado"
    return tarefas, ""


def salvar_tarefas(tarefas):
    try:
        os.makedirs(PASTA, exist_ok=True)
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    except OSError as erro:
        print("Erro ao salvar o arquivo:", erro)
        return "Não foi possível salvar as tarefas: " + str(erro)
    return ""


def ordem(tarefa):
    return datetime.strptime(tarefa["data"] + " " + tarefa["hora"], "%d/%m/%Y %H:%M")


def ordenar_tarefas(tarefas):
    tarefas.sort(key=ordem)