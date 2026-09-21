Jogadores = ["Lucas", "Gabriel", "Rafael", "Pedro", "André"]
Gols = [4, 7, 15, 9, 5]
soma = 0
def calcularTotalGols(Gols):
    for gol in Gols:
        soma+=gol
    return soma
def calcularMediaGols(Gols):
    for gol in Gols:
        soma+=gol
    media = soma/ len(Gols) 
    return media


print(f"A media de gols foi:{calcularMediaGols(Gols)}")

print(f"O total de gols foi: {calcularTotalGols(Gols)}")




# def encontrarArtilheiros():
# def mostrarRelatorio():
