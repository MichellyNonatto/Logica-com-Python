'''Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.z'''

def calculoPecas():
    insert = input()
    insert = insert.split()
    values = list(map(float, insert))

    calc = values[1]*values[2]
    return calc


calc1 = calculoPecas()
calc2 = calculoPecas()

print(f"VALOR A PAGAR: R$ {calc1+calc2:.2f}")

#   fonte: BeeCrowd