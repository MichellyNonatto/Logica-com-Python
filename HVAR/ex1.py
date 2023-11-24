import sys

for line in sys.stdin:
    i, j = map(int, line.rstrip().split())


    max_comprimento = 0
    numero_max_comprimento = 0


    for numero in range(i, j + 1):
        n = numero
        quantidade, valor_maximo = 1, n

        while n != 1:
            if n % 2 == 0:
                resultado = n / 2
            else:
                resultado = (n * 3) + 1

            n = resultado

            quantidade += 1
            valor_maximo = resultado if resultado > valor_maximo else valor_maximo

        if quantidade > max_comprimento:
            max_comprimento = quantidade
            numero_max_comprimento = numero

    print(f"{i} {j} {max_comprimento}")
