# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:40:26 2020

@author: Matheus
"""

from numpy.random import randint
from numpy import argsort, unique


class Populacao:
    """
	Cria	e	avalia	uma	população.
	Recebe	como	entrada: recebe	um	indivíduo	como	entrada	e retorna
	um	valor	numérico.   
      cromossos_totais	-	Número	inteiro	representando	o	tamanho da	cadeia
      o	inteiro	representando o tamanho da	cadeia
      genética	do	indivíduo.
      tamanho_populacao	-	Número	inteiro	representando o número total de indivíduos	na	população.

	"""

    def __init__(self, avaliacao, genes_totais, tam_populacao):
        self.avaliacao = avaliacao
        self.genes_totais = genes_totais
        self.tam_populacao = tam_populacao

    def gerar_pop(self):
        """
        Gerador de popupalçao aleatoria

        Returns
        -------
        None.

        """

        self.populacao = randint(0, 2, size=(self.tam_populacao, self.genes_totais), dtype='b')

    def avaliar(self):
        """
        Avalia e ordena a populacao

        Return
        -------
        None.

        """

        u, indices = unique(self.populacao, return_inverse=True, axis=0)
        valores = self.avaliacao(u)
        valores = valores[indices]
        ind = argsort(valores)
        self.populacao[:] = self.populacao[ind]
        return valores[ind]
