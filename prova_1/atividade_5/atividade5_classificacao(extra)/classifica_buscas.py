from collections import Counter
import pandas as pd
#abre busca csv
df = pd.read_csv('busca.csv')
#dados
X_df = df[['home', 'busca', 'logado']]
#classificação
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_treino = 0.9

tamanho_de_treino = int(porcentagem_treino * len(Y))
tamanho_de_teste = len(Y) - tamanho_de_treino

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

#manda o sistema dar o palpite
resultado = modelo.predict(teste_dados)
acertos = (resultado == teste_marcacoes)

#pega elementos acertados e total
total_de_acertos = sum(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(f"total de elementos no df: {total_de_elementos}")
print("Taxa de acerto do algoritmo: %f" % taxa_de_acerto)


# a eficácia do algoritmo que chuta tudo um único valor
acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(teste_marcacoes)
print("Taxa de acerto algoritomo que chuta so umma valor: %f" % taxa_de_acerto_base)
