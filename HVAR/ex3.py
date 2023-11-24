import sys

lista = []

for line in sys.stdin:
    line = line.rstrip()
    lista.append(list(map(str, line.rstrip().split())))

    ocorrencias_cidades = {}

    for i in range(1, len(lista)):
        cidade_nome = lista[i][1]
        if cidade_nome not in ocorrencias_cidades:
            ocorrencias_cidades[cidade_nome] = 0 
        ocorrencias_cidades[cidade_nome] += 1

    resultado = []

    for cidade_nome, contagem in ocorrencias_cidades.items():
        resultado.append((cidade_nome, contagem))

    resultado.sort(key=lambda x: x[0])

    for cidade_nome, contagem in resultado:
        print(cidade_nome, contagem)
