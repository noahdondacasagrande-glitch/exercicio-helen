nomes = ["dipirona", "paracetamol", "loratadina", "ibuprofeno", "omeprazol"]
precos = [12.50, 9.90, 18.75, 15.00, 22.30]
estoques = [20, 15, 8, 3, 2]
posicao = 0

def listarMedicamentos():
    print("tabela de remedios")
    for i in range(len(nomes)):
        print(f"Remedio:{nomes[i]} Preço: R${precos[i]:.2f} Estoque: {estoques[i]} unidades")

def pesquisarMedicamento(nomes):
    medicPes= input("qual medicamento voce quer?")
    pesquisa =[]
    for i in range(len(nomes)):
        posicao+=1
        if i == medicPes:
            pesquisa[i] = nomes(i)
    return  print(f"Remedio:{pesquisa[posicao]} Preço: R${precos[posicao]:.2f} Estoque: {estoques[posicao]} unidades")


    


# def registrarVenda():
# def reporEstoque():
# def verificarEstoqueBaixo():

def menu():
    while True:
        print("1 - Listar medicamentos")
        print("2 - Pesquisar medicamento")
        print("3 - Registrar venda")
        print("4 - Repor estoque")
        print("5 - Verificar estoque baixo")
        print("6 - Sair")

        escolha = input("Escolha uma opção(1-6): ")

        if escolha == "1":
            listarMedicamentos()  
        elif escolha == "2":
            pesquisarMedicamento(nomes, posicao)  
        # elif escolha == "3":
        #     registrarVenda()
        # elif escolha == "4":
        #     reporEstoque() 
        # elif escolha == "5":
        #     verificarEstoqueBaixo() 


menu()
