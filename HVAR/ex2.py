import sys
for line in sys . stdin :
    salario = list(map(int, line.rstrip().split()))

    maior, menor = salario[0], salario[0]

    for i in salario:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i

    for i in salario:
       if i < maior and i > menor: 
            salvo = i

    print(salvo)