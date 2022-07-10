import questão_4A as q4
import numpy as np
import matplotlib.pyplot as plt

#duas listas do arquivo anterior
lista_1 = q4.nao_ordenado
lista_2 = q4.ordernado

#grupo_1 não ordenados
np.random.seed(1)
x = np.array(range(10))
y = np.array(lista_1)
#grupo_2 ordenados
np.random.seed(2)
x_1 = np.array(range(10))
y_1 = np.array(lista_2)

largura = 0.50

fig, ax = plt.subplots()
grupo_1 = ax.bar((x - largura/2), y, largura, label= "nao_ordenados", color = "turquoise")
grupo_2 = ax.bar((x_1 + largura/2), y_1, largura, label= "ordenados", color = "y")
ax.set_title("Arranjos não ordenado e ordenado")
ax.legend()
plt.show()