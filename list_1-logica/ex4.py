'''Cimba herdou um terreno em formato triangular após o falecimento de seu pai. Para passar o terreno para seu nome, o cartório exige que seja informada a área do terreno. Sabe-se que o terreno é delimitado por uma cerca e Cimba consegue medir cada um dos lados do terreno. Você consegue ajudar Cimba a calcular a área do terreno dadas as medidas dos lados?'''

#   Fórmula de Heron

def area_terreno(lista):
    lista = lista.split()
    a, b, c = map(float, lista)
    p = (a+b+c)/2
    area = pow(p*((p-a)*(p-b)*(p-c)), 1/2)
    return area

print(f"{area_terreno(input()):.3f} m2")