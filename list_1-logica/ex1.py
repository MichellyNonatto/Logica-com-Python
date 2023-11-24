"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
"""
def diferencaProduto(listNotas, listProduto=[]):
    if len(listNotas) > 1:
        produto = listNotas[0] * listNotas[1]
        listProduto.append(produto)
        return diferencaProduto(listNotas[2:], listProduto)
    else:
        subtracao = listProduto[0]
        for i in listProduto[1:]:
            subtracao -= i
        return subtracao

list = [int(input()) for i in range(4)]
print(f"DIFERENCA = {diferencaProduto(list)}")

#   fonte: BeeCrowd