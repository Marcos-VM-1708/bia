# preparando ambiente
#ttps://colab.research.google.com/drive/1-NEUKmnHFBpf_Odg72XgxOxwp_Yw9_Va?usp=sharing
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# pegando o data frame pra pandas
df_total = pd.read_csv('cases-brazil-states.csv')
df_total.head()

# trato o data frame pois na coluna estado implementa "total"
# então ordeno a linhas de 2x2 pegando o maior valor do dia
df = df_total[df_total['estado'] != 'TOTAL']
df['data'] = pd.to_datetime(df_total['data']).dt.date
df.head()
# grafico usando y como a taxa de óbitos/dia
# por padrão as cores foram
# def estados_corona():

plt.figure(figsize=(20, 8))
fig = sns.lineplot(x='data', y='Obitos', hue='estado', data=df)
# adiciono o titulo e deixo em negrito todos testos
fig.set_title('Óbitos por estado / tempo', loc='left', fontsize=24)
fig.set_xlabel('Data', fontsize=24)
fig.set_ylabel('Óbitos', fontsize=24)

# decidi trabalhar com sp pois tem mais indeces de corona

# df_sp.head()
df_sp = df[df['estado'] == 'SP']
df_sp.head()

# grafico barras
plt.figure(figsize=(20, 8))
fig = plt.bar(df_sp.data, df_sp.suspeitos, label='Suspeitos')
plt.bar(df_sp.data, df_sp.recuperados, label='Recuperados')
plt.bar(df_sp['data'], df_sp['Obitos'], label='Óbitos')
plt.xlabel('Data', fontsize=24)
plt.ylabel('Óbitos, Recuperados e Suspeitos', fontsize=24, rotation=90)
plt.legend()
#implementação do metodo por criador
def plotar_barra(titulo, xlabel, ylabel, x, y, dataset):
    plt.figure(figsize=(20, 6))
    ax = plt.bar(dataset[x], dataset[y])
    plt.title(titulo, loc='left', fontsize=20)
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20, rotation=90)
#exemplo
plotar_barra('Novos casos (SP)', 'Data', 'Novos casos', 'data', 'novosCasos', df_sp)