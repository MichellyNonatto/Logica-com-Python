'''
Nós temos alguns textos e queremos formatá-los e justificá-los à direita, ou seja, alinhar suas linhas à margem direita de cada um. Crie um programa que, após ler um texto, reimprima esse texto com apenas um espaço entre as palavras e suas linhas justificadas à direita em todo o texto.
'''

def formatar(lista_texto):
    max = 0
    for i in range(len(lista_texto)):

        palavra = list(lista_texto[i].split())
        
        lista_texto[i] = " ".join(palavra)

        if len(lista_texto[i]) > max:
            max = len(lista_texto[i])

    for i in range(len(lista_texto)):    
        lista_texto[i] = lista_texto[i].rjust(max)
    
    return lista_texto


formatacao = []
while True:
    teste = int(input())
    if teste == 0 :
        break

    lista_texto = []
    
    for i in range(teste):
        texto = input().upper()
        lista_texto.append(texto)

    formatacao.append(formatar(lista_texto))

for i in range(len(formatacao)):
    for j in formatacao[i]:
        print(j)
    if i != len(formatacao)-1:
        print('')


# fonte: BeeCrowd