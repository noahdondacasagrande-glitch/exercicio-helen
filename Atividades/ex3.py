nomes = ["dipirona", "paracetamol", "loratadina", "ibuprofeno", "omeprazol"]
precos = [12.50, 9.90, 18.75, 15.00, 22.30]
estoques = [20, 15, 8, 3, 2]

def listarremedios():
    print("Lista de remedios")
    for i in range(len(nomes)):
        print(f"O produto {nomes[i]} tem preço de {precos[i]:.2f} e está com {estoques[i]} unidades em estoque")

def pesquisarremedio():
    termo = input("Nome do remedio:")
    if termo in nomes:
        for i in range(len(nomes)):
            if nomes[i] == termo:
                print(f"O remedio {nomes[i]} custa R$ {precos[i]:.2f}  e tem {estoques[i]} unidades")
    else:
        print("remedio não encontrado.")

def registrarVenda():
    nomeRe = input("Remedio vendido: ")
    if nomeRe in nomes:
        for i in range(len(nomes)):
            if nomes[i] == nomeRe:
                quantidade = int(input("Digite a quantidade vendida: "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero")

                elif quantidade > estoques[i]:
                    print(f"Sem remedio. quantidade atual: {estoques[i]} ")
                else:
                    estoques[i] = estoques[i] - quantidade
                    print(f"Novo estoque: {estoques[i]} ")
    else:
        print("remedio não encontrado.")

def reporEstoque():
    termo = input("Digite o nome do remedio:  ")
    if termo in nomes:
        for i in range(len(nomes)):
            if nomes[i] == termo:
                qtd = int(input("Digite a quantidade a ser adicionada ao estoque: "))
                if qtd <= 0:
                    print("A quantidade deve ser maior que zero.")
                else:
                    estoques[i] = estoques[i] + qtd
                    print(f"Novo estoque: {estoques[i]} unidades.")
    else:
        print("remedio não encontrado.")

def verificarEstoqueBaixo():
    print("Baixo estoque")
    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(f"O remedio {nomes[i]} tem {estoques[i]} unidades")

def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1: Listar remedios")
        print("2: Pesquisar remedio")
        print("3: Registrar venda")
        print("4: Repor estoque")
        print("5: Mostrar estoque baixo")
        print("6: Encerrar")
        
        opcao = input("Escolha uma opção (1 a 6): ")
        
        if opcao == "1":
            listarremedios()
        elif opcao == "2":
            pesquisarremedio()
        elif opcao == "3":
            registrarVenda()
        elif opcao == "4":
            reporEstoque()
        elif opcao == "5":
            verificarEstoqueBaixo()
        elif opcao == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")

menu()