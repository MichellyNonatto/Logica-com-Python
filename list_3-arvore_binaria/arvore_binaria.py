class No:

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def obtervalor(self):
        return self.valor

    def setesquerda(self, filhoesquerda):
        self.esquerda = filhoesquerda

    def setdireita(self, filhodireita):
        self.direita = filhodireita

    def obteresquerda(self):
        return self.esquerda
    
    def obterdireita(self):
        return self.direita

class Arvore:
    def __init__(self):
        self.raiz = None

    def obterraiz(self):
        return self.raiz
    
    def inserir(self, dado):
        no = No(dado)

        if self.raiz:
            no_atual = self.raiz
            no_pai = None

            while True:
                if no_atual:
                    no_pai = no_atual
                    if no.obtervalor() < no_atual.obtervalor():
                        no_atual = no_atual.obteresquerda()
                    else:
                        no_atual = no_atual.obterdireita()
                else:
                    if no.obtervalor() < no_pai.obtervalor():
                        no_pai.setesquerda(no)
                    else:
                        no_pai.setdireita(no)
                    break
        else:
            self.raiz = no

    def mostraarvore(self, no_atual):   #   percurso em ordem simétrica
        if no_atual:
            self.mostraarvore(no_atual.obteresquerda())
            print(f"{no_atual.obtervalor()}", end=" ")
            self.mostraarvore(no_atual.obterdireita())


arvore = Arvore()

for i in range(4):
    arvore.inserir(int(input('insira um valor:\t')))

arvore.mostraarvore(arvore.obterraiz())