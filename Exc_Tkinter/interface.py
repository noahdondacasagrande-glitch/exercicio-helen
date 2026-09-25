import tkinter as tk
from tkinter import messagebox

from dados import carregar_tarefas, ordenar_tarefas, salvar_tarefas
from validacoes import validar_data, validar_hora, validar_texto

ROXO = "#5506CC"
AMARELO = "#FFDE5E"
ESCURO = "#333333"
CARD_AMARELO = "#5506CC"
BARRA_AMARELA = "#5506CC"
CARD_AZUL = "#1E75D1"
BARRA_AZUL = "#3333FF"

tarefas, erro_carregar = carregar_tarefas()
tarefa_selecionada = None
tarefa_editando = None
filtro = "todas"


def criar_card(tarefa):
    if tarefa["concluida"]:
        cor_fundo = CARD_AZUL
        cor_barra = BARRA_AZUL
        situacao = "Concluída"
    else:
        cor_fundo = CARD_AMARELO
        cor_barra = BARRA_AMARELA
        situacao = "Pendente"

    
    if tarefa is tarefa_selecionada:
        cor_borda = ROXO
    else:
        cor_borda = "white"

    card = tk.Frame(frame_cards, bg=cor_fundo, highlightthickness=3, highlightbackground=cor_borda)
    card.pack(fill="x", padx=10, pady=6)

    barra = tk.Frame(card, bg=cor_barra, width=12)
    barra.pack(side="left", fill="y")

    titulo = tk.Label(card, text=tarefa["texto"], bg=cor_fundo, anchor="w", font=("Arial", 14, "bold"))
    titulo.pack(fill="x", padx=15, pady=(10, 0))

    subtitulo = tk.Label(card, text=tarefa["data"] + " às " + tarefa["hora"] + "  -  " + situacao,
                         bg=cor_fundo, fg="#4D4D4D", anchor="w", font=("Arial", 11))
    subtitulo.pack(fill="x", padx=15, pady=(0, 10))

    # clicar em qualquer parte do card seleciona a tarefa
    card.bind("<Button-1>", lambda evento: selecionar_tarefa(tarefa))
    titulo.bind("<Button-1>", lambda evento: selecionar_tarefa(tarefa))
    subtitulo.bind("<Button-1>", lambda evento: selecionar_tarefa(tarefa))


def mostrar_tarefas():
    for item in frame_cards.winfo_children():
        item.destroy()

    ordenar_tarefas(tarefas)
    busca = entry_busca.get().strip().lower()
    quantidade = 0

    for tarefa in tarefas:
        if filtro == "pendentes" and tarefa["concluida"]:
            continue
        if filtro == "concluidas" and not tarefa["concluida"]:
            continue
        if busca != "" and busca not in tarefa["texto"].lower() and busca not in tarefa["data"]:
            continue
        criar_card(tarefa)
        quantidade = quantidade + 1

    if quantidade == 0:
        tk.Label(frame_cards, text="Nenhuma tarefa encontrada", bg="white", fg="#B85450",
                 font=("Arial", 13, "bold")).pack(pady=30)

    concluidas = 0
    for tarefa in tarefas:
        if tarefa["concluida"]:
            concluidas = concluidas + 1
    pendentes = len(tarefas) - concluidas
    label_resumo.config(text="Total: " + str(len(tarefas)) + "   Pendentes: " + str(pendentes)
                        + "   Concluídas: " + str(concluidas))
    frame_cards.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


def selecionar_tarefa(tarefa):
    global tarefa_selecionada
    tarefa_selecionada = tarefa
    mostrar_tarefas()


def mudar_filtro(novo_filtro):
    global filtro
    filtro = novo_filtro
    mostrar_tarefas()

def abrir_formulario(tarefa):
    global janela_form, entry_texto, entry_data, entry_hora, var_concluida, tarefa_editando
    tarefa_editando = tarefa

    janela_form = tk.Toplevel(janela)
    janela_form.geometry("420x340")
    janela_form.configure(bg=CARD_AMARELO)
    janela_form.transient(janela)
    janela_form.wait_visibility()

    if tarefa is None:
        janela_form.title("Nova tarefa")
    else:
        janela_form.title("Editar tarefa")

    tk.Label(janela_form, text="Texto da tarefa (até 100 caracteres)", bg=CARD_AMARELO).grid(
        row=0, column=0, sticky="w", padx=20, pady=(20, 0))
    entry_texto = tk.Entry(janela_form, width=45)
    entry_texto.grid(row=1, column=0, padx=20)

    tk.Label(janela_form, text="Data (DD/MM/AAAA)", bg=CARD_AMARELO).grid(
        row=2, column=0, sticky="w", padx=20, pady=(10, 0))
    entry_data = tk.Entry(janela_form, width=20)
    entry_data.grid(row=3, column=0, sticky="w", padx=20)

    tk.Label(janela_form, text="Hora (HH:MM)", bg=CARD_AMARELO).grid(
        row=4, column=0, sticky="w", padx=20, pady=(10, 0))
    entry_hora = tk.Entry(janela_form, width=20)
    entry_hora.grid(row=5, column=0, sticky="w", padx=20)

    var_concluida = tk.BooleanVar(value=False)
    tk.Checkbutton(janela_form, text="Concluída", variable=var_concluida, bg=CARD_AMARELO).grid(
        row=6, column=0, sticky="w", padx=20, pady=10)

    botoes = tk.Frame(janela_form, bg=CARD_AMARELO)
    botoes.grid(row=7, column=0, sticky="w", padx=20)
    tk.Button(botoes, text="Salvar", bg=ROXO, fg="white", width=10, command=salvar_formulario).pack(side="left")
    tk.Button(botoes, text="Cancelar", width=10, command=janela_form.destroy).pack(side="left", padx=10)

    # se for edição, preenche os campos com os dados da tarefa
    if tarefa is not None:
        entry_texto.insert(0, tarefa["texto"])
        entry_data.insert(0, tarefa["data"])
        entry_hora.insert(0, tarefa["hora"])
        var_concluida.set(tarefa["concluida"])

    # Enter salva e Esc fecha
    entry_texto.bind("<Return>", lambda evento: salvar_formulario())
    entry_data.bind("<Return>", lambda evento: salvar_formulario())
    entry_hora.bind("<Return>", lambda evento: salvar_formulario())
    janela_form.bind("<Escape>", lambda evento: janela_form.destroy())
    entry_texto.focus_set()


def salvar_formulario():
    texto = entry_texto.get().strip()
    data = entry_data.get().strip()
    hora = entry_hora.get().strip()

    erro = validar_texto(texto)
    if erro != "":
        messagebox.showwarning("Dados inválidos", erro, parent=janela_form)
        entry_texto.focus_set()
        return
    erro = validar_data(data)
    if erro != "":
        messagebox.showwarning("Dados inválidos", erro, parent=janela_form)
        entry_data.focus_set()
        return
    erro = validar_hora(hora)
    if erro != "":
        messagebox.showwarning("Dados inválidos", erro, parent=janela_form)
        entry_hora.focus_set()
        return

    if tarefa_editando is None:
        nova = {"texto": texto, "data": data, "hora": hora, "concluida": var_concluida.get()}
        tarefas.append(nova)
        mensagem = "Tarefa cadastrada com sucesso"
    else:
        tarefa_editando["texto"] = texto
        tarefa_editando["data"] = data
        tarefa_editando["hora"] = hora
        tarefa_editando["concluida"] = var_concluida.get()
        mensagem = "Tarefa atualizada"

    erro = salvar_tarefas(tarefas)
    if erro != "":
        messagebox.showerror("Erro ao salvar", erro, parent=janela_form)
        return

    janela_form.destroy()
    mostrar_tarefas()
    label_status.config(text=mensagem)

def nova_tarefa():
    abrir_formulario(None)


def editar_tarefa_selecionada():
    if tarefa_selecionada is None:
        messagebox.showwarning("Aviso", "Clique em uma tarefa para selecionar primeiro")
        return
    abrir_formulario(tarefa_selecionada)


def excluir_tarefa_selecionada():
    global tarefa_selecionada
    if tarefa_selecionada is None:
        messagebox.showwarning("Aviso", "Clique em uma tarefa para selecionar primeiro")
        return
    resposta = messagebox.askyesno("Confirmar exclusão", "Deseja realmente excluir esta tarefa?")
    if resposta:
        tarefas.remove(tarefa_selecionada)
        tarefa_selecionada = None
        erro = salvar_tarefas(tarefas)
        if erro != "":
            messagebox.showerror("Erro ao salvar", erro)
        mostrar_tarefas()
        label_status.config(text="Tarefa excluída")


def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair do Tasky?"):
        janela.destroy()


def rolar(evento):
    # roda a rolagem do mouse na lista de tarefas
    if evento.delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")


def criar_botao_menu(texto, cor, comando):
    quadro = tk.Frame(menu, bg="white", highlightbackground="black", highlightthickness=2)
    quadro.pack(fill="x", pady=8)

    icone = tk.Canvas(quadro, width=34, height=34, bg="white", highlightthickness=0)
    icone.create_oval(3, 3, 31, 31, fill=cor, outline="black", width=2)
    icone.pack(side="left", padx=10, pady=8)

    botao = tk.Button(quadro, text=texto, command=comando, bg="white", relief="flat",
                      anchor="w", font=("Arial", 13))
    botao.pack(side="left", fill="x", expand=True, padx=(0, 10))

janela = tk.Tk()
janela.title("Tasky")
janela.geometry("1000x650")
janela.minsize(850, 550)
janela.configure(bg="white")

cabecalho = tk.Frame(janela, bg="white")
cabecalho.pack(fill="x")
tk.Label(cabecalho, text="Tasky", bg="white", fg=ROXO, font=("Arial", 30, "bold")).pack(
    side="left", padx=20, pady=8)
tk.Frame(janela, bg=ROXO, height=4).pack(fill="x")

barra = tk.Frame(janela, bg="white", highlightbackground=ESCURO, highlightthickness=2)
barra.pack(fill="x", padx=20, pady=(12, 0))
tk.Label(barra, text="Pesquisar:", bg="white", font=("Arial", 11)).pack(side="left", padx=(12, 6), pady=10)
entry_busca = tk.Entry(barra, width=30, font=("Arial", 11))
entry_busca.pack(side="left")
entry_busca.bind("<KeyRelease>", lambda evento: mostrar_tarefas())
label_resumo = tk.Label(barra, text="", bg="white", fg=ROXO, font=("Arial", 11, "bold"))
label_resumo.pack(side="right", padx=12)

rodape = tk.Frame(janela, bg=ESCURO)
rodape.pack(side="bottom", fill="x")
tk.Label(rodape, text="Tasky", bg=ESCURO, fg=AMARELO, font=("Arial", 16, "bold")).pack(
    side="left", padx=20, pady=6)
label_status = tk.Label(rodape, text="Pronto", bg=ESCURO, fg="white", font=("Arial", 10))
label_status.pack(side="right", padx=20)

corpo = tk.Frame(janela, bg="white")
corpo.pack(fill="both", expand=True, padx=20, pady=10)

menu = tk.Frame(corpo, bg="white", width=260)
menu.pack(side="left", fill="y")
criar_botao_menu("Nova tarefa", "white", nova_tarefa)
criar_botao_menu("Editar tarefa", "white", editar_tarefa_selecionada)
criar_botao_menu("Excluir tarefa", "white", excluir_tarefa_selecionada)
criar_botao_menu("Concluídas", "#D5E8D4", lambda: mudar_filtro("concluidas"))
criar_botao_menu("Pendentes", "#F8CECC", lambda: mudar_filtro("pendentes"))
criar_botao_menu("Todas", "#DAE8FC", lambda: mudar_filtro("todas"))


area_cards = tk.Frame(corpo, bg="white")
area_cards.pack(side="left", fill="both", expand=True, padx=(20, 0))

canvas = tk.Canvas(area_cards, bg="white", highlightthickness=0)
barra_rolagem = tk.Scrollbar(area_cards, command=canvas.yview)
canvas.configure(yscrollcommand=barra_rolagem.set)
barra_rolagem.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

frame_cards = tk.Frame(canvas, bg="white")
janela_cards = canvas.create_window((0, 0), window=frame_cards, anchor="nw")


def ajustar_largura(evento):
    canvas.itemconfig(janela_cards, width=evento.width)


canvas.bind("<Configure>", ajustar_largura)
janela.bind_all("<MouseWheel>", rolar)


def iniciar():
    if erro_carregar != "":
        messagebox.showerror("Erro ao carregar", erro_carregar + "\n\nO Tasky vai abrir com a lista vazia.")
    mostrar_tarefas()
    janela.protocol("WM_DELETE_WINDOW", sair)
    janela.mainloop()