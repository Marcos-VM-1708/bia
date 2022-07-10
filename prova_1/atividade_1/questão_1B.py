
import numpy as np

boleano = False

tamanho = input("qual a dificudade do caça palavras?(facil, medio, dificil) ").upper()
if tamanho == "FACIL":
    tamanho = 5
elif tamanho == "MEDIO":
    tamanho = 10
elif tamanho == "DIFICIL":
    tamanho = 15


matriz = np.zeros((tamanho, tamanho), dtype='str')

lista_palavra = []
qnt_palavra = int(input("quantas palavras quer implementar"))

for i in range(qnt_palavra):
    string_palavra = input("insira plavra").upper()
    lista_palavra.append(string_palavra)

#pra cada palavra na lista
for palavra in lista_palavra:
    # sorteia se é horizontal ou vertical
    #1 = true vertical
    #0 = false vertical
    vertical = np.random.choice([0, 1])
    count = 1
    possivel = False

    while (possivel == False):
        possivel = True
        #vertical
        if (vertical == 1):
            #defino x e y pra vertical
            x = np.random.choice(range(0, tamanho))
            y = np.random.choice(range(0, tamanho - len(palavra) + 1))

            # Verifica se é possível alocar a palavra, se for, o faz
            if matriz[x][y] == '':
                for i, p in enumerate(palavra):
                    if (matriz[x][y + i] == '' or matriz[x][y + i] == p):
                        possivel = possivel and True  # tudo bem
                    else:
                        possivel = False  # não pode alocar aqui

                if possivel:
                    # Aloca a palavra
                    for i, p in enumerate((palavra)):
                        matriz[x][y + i] = p
                #passando para proxima instancia
                else:
                    count += 1
                    #porixima palavra
            else:
                count += 1

        #horizontal
        else:
            #define x e y pra horizontal
            x = np.random.choice(range(0, tamanho - len(palavra) + 1))
            y = np.random.choice(range(0, tamanho))

            # Verifica se é possível alocar a palavra, se for, o faz
            if matriz[x][y] == '':
                #palavra /
                for i, p in enumerate(palavra):
                    if (matriz[x + i][y] == '' or matriz[x + i][y] == p):
                        possivel = possivel and True  # tudo bem
                    else:
                        possivel = False  # não pode alocar aqui

                if possivel:
                    # Aloca a palavra
                    for i,  p in enumerate((palavra)):
                        matriz[x + i][y] = p
                    #proxima intancia
                else:
                    count += 1
                    # porixima palavra
            else:
                count += 1
        if count > 200:
            # Desiste após 100 tentativas
            possivel = True
def resto_palavras():
    # Preenche o resto com letras
    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] == '':
                matriz[i][j] = np.random.choice(list(map(chr, range(ord("A"), ord("Z")))))
    print(matriz)

resto_palavras()









