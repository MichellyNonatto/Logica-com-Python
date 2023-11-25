# O nó é construido a partir de uma classe

class No:

    def __init__(self, dado):
        self.dado = dado
        self.prox = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self._tamanho = 0

    def adicionar(self, dado):
        if self.inicio:  # Quando a lista já possui elementos

            ponteiro = self.inicio  # aponta para o primeiro elemento da lista

            while (ponteiro.prox):  # enquanto o proximo elemento não for None
                ponteiro = ponteiro.prox

            # faz com que o elemento com o prox vazio receba o novo dado, na qual esse novo dado terá seu nó apontado para None
            ponteiro.prox = No(dado)

        else:
            self.inicio = No(dado)  # primeira inserção a lista

        self._tamanho += 1

        def __len__(self):  # objeto len() que retorna o tamanho da lista
            return self._tamanho

        def __getitem__ (self, posicao): # retorna o valor de uma posição

            #   lista.get(8)
             
            ponteiro = self.inicio

            try:
                for i in range(posicao):
                    ponteiro = ponteiro.prox

                if ponteiro:
                    return ponteiro.dado
            except IndexError:
                return "índice de lista inesistente no vetor"

        def __setitem__(self, posicao, novoElemento):  # modificar um elemento

            #   lista.set(5, 6)

            ponteiro = self.inicio

            try:
                for i in range(posicao):
                    ponteiro = ponteiro.prox
                    
                if ponteiro:
                    ponteiro.dado = novoElemento

            except IndexError:
                return "índice de lista inesistente no vetor"


lista = ListaEncadeada()
lista.adicionar(7)
