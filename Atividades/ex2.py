tentativas = []
valores_aceitos = [0, 1, 2, 3]
c = 1
freq_0 = freq_1 = freq_2 = freq_3 = 0

def registrarTentativas():
    for i in range(0, 10):  
        tentativas.append(int(input(f"digite a {i +1}° tentativa em pontos(emvalores de 0, 1 ,2 ,3): ")))
        while tentativas[i] not in valores_aceitos:
            print("Valor inválido! Insira apenas 0, 1, 2 ou 3.")
            tentativas.pop()  
            tentativas.append(int(input(f"Digite a {i +1}° tentativa em pontos (0, 1, 2, 3")))

def calcularPontuacao():
    soma = 0
    for i in range(len(tentativas)):
        soma+=tentativas[i]
    return soma    

registrarTentativas()
def erros():
    erro = 0
    for i in range(len(tentativas)):
        if tentativas[i] == 0:
            erro+=1
    return erro

def acertos():      
    acerto = 0
    for i in range(len(tentativas)):
        if tentativas[i] > 0:
            acerto+=1
    return acerto

def calcularAproveitamento():
    aproveitamento = (acertos() / len(tentativas)) * 100
    return aproveitamento

def encontrarCestaMaisFrequente():
    f0 = tentativas.count(0)
    f1 = tentativas.count(1)
    f2 = tentativas.count(2)
    f3 = tentativas.count(3)
    
    resultado = max((f0, 0), (f1, 1), (f2, 2), (f3, 3))[1]
    return resultado

     
for t in tentativas:
    print(f"Tentativa {c}°: {tentativas[t]}")
    c+=1

print(f"A soma dos pontos e de: {calcularPontuacao()}")
print(f"bolas acertadas: {acertos()}")
print(f"bolas erradas: {erros()}")
print(f"O aproveitamento foi de {calcularAproveitamento()}%")
print(f"A cesta mais frequente foi: {encontrarCestaMaisFrequente()}")