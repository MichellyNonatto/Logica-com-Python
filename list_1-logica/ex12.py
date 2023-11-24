'''
Você chegou a um dos últimos chefões no novo jogo de ação 2-D de deslocamento lateral, KiloMan. O chefão tem uma arma grande que pode atirar projéteis em várias alturas. Para cada tiro, KiloMan pode ficar parado ou pular. Se ele ficar parado e o tiro estiver na altura 1 ou 2, ele será atingido. Se ele pular e o tiro estiver a uma altura maior que 2, então ele também será atingido. Caso contrário, ele não é atingido. Dada a altura de cada tiro e a sequência de pulos, quantas vezes KiloMan será atingido?
'''

def kiloMan():
    qtd_tiros = int(input())
    altura_tiro = list(map(int, input().split()))

    if len(altura_tiro) == qtd_tiros:
        acoes = input().lower()
        atingido = 0
        for i in range(len(acoes)):
            if acoes[i] == 'j' and altura_tiro[i] > 2:
                atingido += 1
            elif acoes[i] == 's' and altura_tiro[i] <= 2:
                atingido += 1
        return atingido
    


lista_resultado = []
n = int(input())

for i in range(n):
    lista_resultado.append(kiloMan())

for i in lista_resultado:
    print(i)

# font: BeeCrowd