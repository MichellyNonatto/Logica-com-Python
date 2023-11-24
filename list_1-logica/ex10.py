'''
Depois de séculos de escaramuças entre os quatro povos habitantes da Nlogônia, e de dezenas de anos de negociações envolvendo diplomatas, políticos e as forças armadas de todas as partes interessadas, com a intermediação da ONU, OTAN, G7 e SBC, foi finalmente decidida e aceita por todos a maneira de dividir o país em quatro territórios independentes.

Ficou decidido que um ponto, denominado ponto divisor, cujas coordenadas foram estabelecidas nas negociações, definiria a divisão do país, da seguinte maneira. Duas linhas, ambas contendo o ponto divisor, uma na direção norte-sul e uma na direção leste-oeste, seriam traçadas no mapa, dividindo o país em quatro novos países. Iniciando no quadrante mais ao norte e mais ao oeste, em sentido horário, os novos países seriam chamados de Nlogônia do Noroeste, Nlogônia do Nordeste, Nlogônia do Sudeste e Nlogônia do Sudoeste.




A ONU determinou que fosse disponibilizada uma página na Internet para que os habitantes pudessem consultar em qual dos novos países suas residências estão, e você foi contratado para ajudar a implementar o sistema.

'''

def localizacao(k, n, m):
    lista_cosulta = []

    for i in range(k):
        x, y = map(int, input().split())

        if x == n or y == m:
            lista_cosulta.append("divisa")

        elif x > n and y > m:
            lista_cosulta.append("NE")

        elif x < n and y > m:
            lista_cosulta.append("NO")

        elif x < n and y < m:
            lista_cosulta.append("SO")

        elif x > n and y < m:
            lista_cosulta.append("SE")

    return lista_cosulta


lista_localizacao = []
while True:

    k = int(input())
    if k == 0:
        break

    n, m = map(int, input().split())
    lista_localizacao.append(localizacao(k, n, m))

for i in lista_localizacao:
    for j in i:
        print(j)


# fonte: BeeCrowd