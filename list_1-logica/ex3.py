'''Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.'''

valor = input()
valores = valor.split() #   converte a string em uma lista de strings
a, b, c, = map(float, valores) #    converte a lista de strings em um float atribuindo a várias variáveis.


def bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0 or 2*a == 0:
        return "Impossivel calcular"
    
    raiz = pow(delta, 1/2) #    raiz quadrada de delta

    r1 = (-(b) + raiz) / (2*a)
    r2 = (-(b) - raiz) / (2*a)

    return f"R1 = {r1:.5f}\nR2 = {r2:.5f}"

print(bhaskara(a, b, c))

#   fonte: BeeCrowd | 1036