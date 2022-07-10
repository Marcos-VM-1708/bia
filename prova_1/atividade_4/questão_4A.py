import random

def ordenacao_selecao(A):
    #crio uma variavel None para implementala em A mais tarde
    null = type(None)
    cont = 0
    #torna-se obrigatorio definir 0 para execulção pois caso contrari o codigo reconhece n como not defined
    n = 0
    #cerifico se possi um valor neutro dentro de A,como nesse caso sempre é não eu appendo None em A para
    #poder usar a verificação do codigo base

    if None is not A:
        A.append(null)
    #nota-se que while pode ser trocado por uma resolução tanto em for ou através dos metodos len() e sort()
    while True:
       #troco "null" por um valor neutro valido em python(None)
       if A[cont] == type(None):
           A.pop()#retiro o valor nono para não ser enserido na saida final
           n = cont #atribui o valor de N para o proximo for
           break#quebro o loop

       else:
        cont += 1
#verifivação elemento por elemento ate estarem todos ordernados
    for i in range(n):
        minimo = i

        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j

        A[i], A[minimo] = A[minimo], A[i]

A = random.sample(range(-10, 10), 10)

def executa():
    print("Arranjo não ordenado: ", A)
    ordenacao_selecao(A)
    print("Arranjo ordenado:", A)
nao_ordenado= list(A)
executa()
ordernado = list(A)



