from numpy import exp, array, mgrid
from pygeneric.populacao import Populacao
from pygeneric.selecao.roleta import Roleta
import matplotlib.pyplot as plt


def func(x, y):
    temp = 3 * exp(-(y + 1) ** 2 - x ** 2 * (x - 1) ** 2) \
           - (exp(-(x + 1) ** 2 - y ** 2) / 3 + exp(-x ** 2 - y ** 2) / 3) \
           + exp(-x ** 2 - y ** 2) * (10 * x ** 3 - 2 * x + 10 * y * 5)

    return temp


def bin(x):
    cnt = array([2 ** i for i in range(x.shape[1])])
    return array([(cnt * x[i, :]).sum() for i in range(x.shape[0])])


"""
    A função xy recebera uma população,
    extrai o numero de colunas do vetor populaçao passado
    metade	da	codificação	genética	será	usada	para
    representar	a variável	x
    enquanto a outra metade	representará a
    variável y
"""
def xy( populacao ):
    colunas = populacao.shape[1]
    meio = colunas // 2
    maiorbin = 2.0 ** meio - 1.0
    nmin = -3
    nmax = 3
    const = (nmax - nmin) / maiorbin
    x = nmin + const * bin(populacao[:, :meio])
    y = nmin + const * bin(populacao[:, meio:])
    return x, y


def avaliacao(populacao):
    x, y = xy(populacao)
    tmp = func(x, y)
    return tmp


############ Testes CAP 2##################

genes_totais = 8
tam_populacao = 100
populacao =	Populacao(avaliacao,genes_totais,tam_populacao)
populacao.gerar_pop()

roleta=	Roleta(populacao)

pop	=roleta.selecao(10)

x,y =xy(pop)

###################GRAFICO##############################
fig	= plt.figure(figsize=(100,	100))

ax=fig.add_subplot(111,	projection="3d")
X,Y=mgrid[-3:3:30j,	-3:3:30j]
Z=func(X,Y)
ax.plot_wireframe(X,	Y,	Z)
ax.scatter(x,	y,	func(x,	y),	s=50,	c='red',	marker='D')
plt.show()




