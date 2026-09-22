Jogadores = ["Lucas", "Gabriel", "Rafael", "Pedro", "André"]
Gols = [4, 7, 15, 9, 5]

def calcularTotalGols(Gols):
    soma = 0
    for gol in Gols:
        soma += gol
    return soma

def calcularMediaGols(Gols):
    soma = 0
    for gol in Gols:
        soma += gol
    media = soma / len(Gols)
    return media

def encontrarArtilheiros():
    maior = Gols[0]
    for gol in Gols:
        if gol > maior:
            maior = gol

    artilheiros = []
    for i in range(len(Gols)):
        if Gols[i] == maior:
            artilheiros.append(Jogadores[i])
    return artilheiros


def mostrarRelatorio(Jogadores, Gols):
    for i in range(len(Jogadores)):
        print(f" O jogador {Jogadores[i]} fez {Gols[i]} gols.")

def assimaMedia(Jogadores,Gols):
    for i in range(len(Gols)):
        if Gols[i] >= calcularMediaGols(Gols):
            print(f"O jogador {Jogadores[i]} fez mais gols que a media")




print(f"A média de gols foi: {calcularMediaGols(Gols)}")

print(f"O total de gols foi: {calcularTotalGols(Gols)}")

print(f"Os artilheiros foram: {encontrarArtilheiros()}")

print(mostrarRelatorio(Jogadores, Gols))

print(assimaMedia(Jogadores,Gols))