'''João e Maria são amigos desde que se conheceram na creche. Desde então, eles compartilham uma rotina de brincadeiras: todas as vezes que eles se encontram, eles jogam Cara ou Coroa com uma moeda, e quem ganhar tem o privilégio de decidir quais brincadeiras eles irão jogar durante o dia. Maria sempre escolhe cara, e João sempre escolhe coroa.

Hoje em dia eles estão na faculdade, mas continuam sendo bons amigos. Sempre que se encontram, eles ainda jogam Cara ou Coroa, e o vencedor decide que filme assistir, ou em que restaurante jantar, e assim por diante.

Ontem Maria contou a João que ela guarda um registro de todas as vezes que eles jogaram, desde os tempos da creche. João ficou espantado. Porém João está estudando Ciência da Computação e decidiu que essa era uma boa oportunidade para mostrar a Maria suas habilidades em programação, escrevendo um programa que mostrasse o número de vezes que cada um deles venceu ao longo de todos esses anos.'''

def contarPontos(lista_pontos):
    m, j = 0, 0

    for vencedor in lista_pontos:
        if vencedor == 0: m += 1
        else: j += 1
    
    return [m, j]

resultado = []
while True:
    n = int(input())
    if n == 0:
        break

    lista_resultados = list(map(int, input().split()))

    if len(lista_resultados) == n:
       resultado.append(contarPontos(lista_resultados))
    else:
        print("Invalid")

for i in resultado:
    print(f'Mary won {i[0]} times and John won {i[1]} times')

# font: BeeCrowd