import random

dificudade = "FACIL"
#input("insira a dificudade(facil, medio, dificio)").upper()

if dificudade == "FACIL":
    escala = 10
elif dificudade == "MEDIO":
    escala = 25
elif dificudade == "DIFICIO":
    escala = 40
    escala = int(escala)



matriz = []
for linha in range(0, escala):
    matriz.append([])
    for coluna in range(0, escala):
        matriz[linha].append("-")


# Pra adicionar as palavras em posições aleatórias
def add_palavra(palavra, matriz):
    linha = random.randint(0, 19)
    coluna = 0
    for i in range(0, len(palavra)):
        matriz[linha][coluna + i] = palavra[i]
        print(palavra(i))
#add_palavra(["porra"], matriz)

def insere_letras(caca_palavras, x):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for linha in range(0, x):
        for coluna in range(0, x):
            if caca_palavras[linha][coluna] == "-":
                randomLetter = random.choice(letras)
                caca_palavras[linha][coluna] = randomLetter

meia = escala / 2



def formato(matriz , x):
    print(" ~" * int(escala + 1)  )
    print("Caça-Palavras")
    for linha in range(0, x):
        line = "| "
        for coluna in range(0, x):
            line = line + matriz[linha][coluna] + " "
        line = line + "|"
        print(line)
    print(" ˜" * (escala + 1))

#insere_letras(matriz, escala)


formato(matriz, escala)

add_palavra("porra" ,matriz)

