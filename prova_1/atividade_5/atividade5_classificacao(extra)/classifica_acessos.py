from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB
X, Y = carregar_acessos()

#parcela do df para treinamento 90%
#dado ja classificados
treino_dados = X[:90]
treino_marcacoes = Y[:90]

#parcela do df pra verificar eficacia 10%
#dados não classificados
teste_dados = X[-10:]
teste_marcacoes = Y[-10:]

#treina o sistema com os 90% ja definidos
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

#chama o sistema para pra tentar classificar
#os 10% não definidos
resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes
#puxo o numero de acertos e elementos
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

#pego a taxa de acertos em %
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(f"total de elementos{total_de_elementos}")
print(f"taxa de acerto para acessos: {taxa_de_acerto}")
