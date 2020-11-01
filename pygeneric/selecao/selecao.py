from numpy import array

class Selecao:
    """
        Seleciona os individuos para cruzamento
        Recebe como entrada:
            populacao - Objeto criado a partir  da classe Populacao

     """
    def __init__(self,populacao):
        self.populacao = populacao
    
    def selecionar(self,fitness):
        """
            Retorna  a lista do indice do vetor  populacao
            dos indivíduos selecionados
        """
        raise NotImplementedError("A ser implementado")

    def selecao (self, n ,fitness = None):
        """
		    Retorna	uma	população	de	tamanho	n,
		    selecionada	via	método	selecionar.
	    """
        progenitores = array([self.selecionar(fitness) for _ in	range(n)])


        return self.populacao.populacao[progenitores]
    

