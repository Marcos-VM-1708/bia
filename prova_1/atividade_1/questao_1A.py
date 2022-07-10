
def main():
#input de palavras
    s = "programacao"
    f = "aprovado"
#instancia onde a segunda palavra(f) vai ser implementada na palavra(s)
    c = input('Entre com a letra para a alocação:')

# quantas letras existem e em que posições?
    lst = []
#cria um loop com o metodo enumerate para percorrer a string(s) devolvendo a letra e a posição
    for pos,char in enumerate(s):
        #se a letra(s) for igual a instancia(c) adiciona a posição na lista slt resultado[5, 7, 9]
        if(char == c):
            lst.append(pos)
#vamos imprimir a letra usando a posicao 2 da lista
    print("posições onde foi encontrada ")
#pega as posiçoes em que a letra(s) foi igual a intancia(c) e escolhe a segunda posição
#ressalta para caso a instancia(c) < 2 o codigo quebra obrigando c = "a", "o", "r"
    lposi = lst[1]
#contador
    x = 0
#pecorre a string(s) procurando a segunda posição da lposi
#se x for = a posição 2 de (s) escreve a palavra
#caso contrario o contador atribui valor mais 1 ate achar a posição 2 de lposi
    for l in s:
        if x == lposi:
            print(f)
        else:
            print(l)
            x+=1
#chama a função
main()