import pandas as pd
import numpy as np
import retorna_doenca as rd

#lendo o arquivo contido no colab na pastinha ao lado, nao se esqueca de enviar o mesmo.
pacientes = pd.read_excel('dadosmedicossaude.xlsx')
lista = pacientes.values.tolist()

#infos do data frame
altura = pacientes["altura"]
peso = pacientes["peso"]
risco = pacientes["risco cardiaco"]

#pego o imc por array n
imc = peso / altura**2
imc_list = np.array(imc)
#adiciono "imc" como coluna no arquivo

pacientes["imc"] = imc

imc = pacientes["imc"]

#valor + e - em escala 1x para ser parametro
valor_menor = min(imc)
valor_maior = max(imc)

#separação de todos elementos com imc = + e -
minimos = pacientes.loc[pacientes["imc"] == valor_menor]
maximos = pacientes.loc[pacientes["imc"] == valor_maior]

#busca a lista de acima do peso se tem risco cardiaco
for x in maximos["risco cardiaco"]:
    if x == "Risco":
        riscos_maximo = x
#busca a lista de abaixo do peso se tem risco cardiaco
for x in minimos["risco cardiaco"]:
    if x == "Risco":
        riscos_minimos = x

#apenas a saida aqui para deixa mais limpo o codigo
#explicação no outro arquivo
def saida(minimos, maximos, imc  ):
    print(f"imc medio de todos pacientesda lista: {imc.mean()}\n")

    print(f"os paciente com maior risco de vida foram definedos entre os seguistes:\n")

    print(f"pacientes com obesidade III")
    print(maximos[["nome do paciente anonimizado", "risco cardiaco","imc"]],"\n")

    print(f"pacientes com desnutriçao:")
    print(minimos[["nome do paciente anonimizado", "risco cardiaco", "imc"]],"\n")

saida(minimos, maximos, imc)

#faixa
while True:
    con = int(input("caso queira consultar o imc de outros pacientes favor inserir numero de inscrição()caso contrario insira 0 "))
    genero = input("sexo do paciente F = female, M = male: ").upper()
    imc = imc_list[2]
    if con == 0:
        break
    else:
        rd.taxa(imc, genero)
