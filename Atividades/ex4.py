def criar_mapa_assentos():
    return [["L" for coluna in range(6)] for fileira in range(5)]

def mostrarAssentos(matriz):
    colunas = ["A", "B", "C", "D", "E", "F"]
    cabecalho = "   "
    for coluna in colunas:
        cabecalho += coluna + "  "
    print(cabecalho)

    for indice_fileira in range(5):
        numero_fileira = indice_fileira + 1
        assentos_texto = ""
        for elemento in matriz[indice_fileira]:
            assentos_texto += elemento + "  "
        print(f"{numero_fileira}  {assentos_texto}")

def validarAssento(assento_texto):
    assento_texto = assento_texto.strip().upper()
    if len(assento_texto) < 2:
        return -1, -1

    parte_fileira = assento_texto[:-1]
    parte_coluna = assento_texto[-1]

    fileiras_validas = ["1", "2", "3", "4", "5"]
    colunas_validas = ["A", "B", "C", "D", "E", "F"]

    if parte_fileira in fileiras_validas and parte_coluna in colunas_validas:
        indice_linha = fileiras_validas.index(parte_fileira)
        indice_coluna = colunas_validas.index(parte_coluna)
        return indice_linha, indice_coluna
    
    return -1, -1

def verificarDisponibilidade(matriz, indice_linha, indice_coluna):
    return matriz[indice_linha][indice_coluna] == "L"

def calcularPreco(indice_linha):
    if indice_linha == 0:
        return "Executiva", 850.00
    elif indice_linha in [1, 2]:
        return "Espaço extra", 600.00
    else:
        return "Econômica", 400.00

def comprarAssento(matriz):
    assento_entrada = input("Assento desejado: ").strip().upper()
    indice_linha, indice_coluna = validarAssento(assento_entrada)

    if indice_linha == -1 or indice_coluna == -1:
        print("Assento inválido! Certifique-se de digitar uma fileira entre 1-5 e coluna entre A-F (ex: 2C).")
        return

    if not verificarDisponibilidade(matriz, indice_linha, indice_coluna):
        print(f"O assento {assento_entrada} já está ocupado.")
        print("Escolha outro assento.")
        return

    categoria, preco = calcularPreco(indice_linha)
    print(f"Categoria: {categoria}")
    print(f"Valor: R$ {preco:.2f}".replace('.', ','))

    confirmacao = input("Confirmar compra? (S/N): ").strip().upper()
    if confirmacao == 'S':
        matriz[indice_linha][indice_coluna] = "O"
        print("Compra realizada com sucesso.")
        print(f"O assento {assento_entrada} agora está indisponível.")
    else:
        print("Compra cancelada pelo passageiro.")

def consultarAssento(matriz):
    assento_entrada = input("Informe o assento para consulta: ").strip().upper()
    indice_linha, indice_coluna = validarAssento(assento_entrada)

    if indice_linha == -1 or indice_coluna == -1:
        print("Assento inválido!")
        return

    categoria, preco = calcularPreco(indice_linha)
    status_assento = "Livre" if matriz[indice_linha][indice_coluna] == "L" else "Ocupado"

    print(f"Assento: {assento_entrada}")
    print(f"Categoria: {categoria}")
    print(f"Preço: R$ {preco:.2f}".replace('.', ','))
    print(f"Status: {status_assento}")

def mostrarResumo(matriz):
    assentos_livres = 0
    assentos_ocupados = 0
    faturamento_total = 0.0

    for indice_linha in range(5):
        for indice_coluna in range(6):
            if matriz[indice_linha][indice_coluna] == "L":
                assentos_livres += 1
            else:
                assentos_ocupados += 1
                categoria, preco = calcularPreco(indice_linha)
                faturamento_total += preco

    total_assentos = 30
    percentual_ocupacao = (assentos_ocupados / total_assentos) * 100

    print("--- RESUMO DO VOO ---")
    print(f"Assentos livres: {assentos_livres}")
    print(f"Assentos ocupados: {assentos_ocupados}")
    print(f"Percentual de ocupação: {percentual_ocupacao:.2f}%")
    print(f"Faturamento total: R$ {faturamento_total:.2f}".replace('.', ','))

def main():
    matriz = criar_mapa_assentos()

    while True:
        print("1 - Visualizar assentos")
        print("2 - Comprar assento")
        print("3 - Consultar assento")
        print("4 - Mostrar resumo do voo")
        print("5 - Encerrar")

        opcao_escolhida = input("Escolha uma opção: ").strip()

        if opcao_escolhida == "1":
            mostrarAssentos(matriz)
        elif opcao_escolhida == "2":
            comprarAssento(matriz)
        elif opcao_escolhida == "3":
            consultarAssento(matriz)
        elif opcao_escolhida == "4":
            mostrarResumo(matriz)
        elif opcao_escolhida == "5":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 5.")

main()