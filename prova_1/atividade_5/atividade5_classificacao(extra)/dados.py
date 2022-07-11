import csv
#pega acessos.csv e trata ele
def carregar_acessos():

	X = []
	Y = []
#abrir
	arquivo = open('acesso.csv', 'r')
	leitor = csv.reader(arquivo)

	next(leitor)
#puxa elementos e passa value
	for home, como_funciona, contato, comprou in leitor:

		dado = [int(home), int(como_funciona), int(contato)]
		X.append(dado)
		Y.append(int(comprou))
	return X, Y

def carregar_buscas():

	X = []
	Y = []
#abrir
	arquivo = open('busca.csv', 'r')
	leitor = csv.reader(arquivo)

	next(leitor)
#loop pra pegar value do csv
	for home, busca, logado, comprou in leitor:

		dado = ([int(home), busca, int(logado)])
		X.append(dado)
		Y.append(int(comprou))

	return X, Y