'''
O professor João decidiu aplicar somente provas de múltipla escolha, para facilitar a correção. Em cada prova, cada questão terá cinco alternativas (A, B, C, D e E), e o professor vai distribuir uma folha de resposta para cada aluno. Ao final da prova, as folhas de resposta serão escaneadas e processadas digitalmente para se obter a nota de cada aluno. Inicialmente, ele pediu ajuda a um sobrinho, que sabe programar muito bem, para escrever um programa para extrair as alternativas marcadas pelos alunos nas folhas de resposta. O sobrinho escreveu uma boa parte do software, mas não pode terminá-lo, pois precisava treinar para a Maratona de Programação.

Durante o processamento, a prova é escaneada usando tons de cinza entre 0 (preto total) e 255 (branco total). Após detectar os cinco retângulos correspondentes a cada uma das alternativas, ele calcula a média dos tons de cinza de cada pixel, retornando um valor inteiro correspondente àquela alternativa. Se o quadrado foi preenchido corretamente o valor da média é zero (preto total). Se o quadrado foi deixado em branco o valor da média é 255 (branco total). Assim, idealmente, se os valores de cada quadrado de uma questão são (255, 0, 255, 255, 255), sabemos que o aluno marcou a alternativa B para essa questão. No entanto, como as folhas são processadas individualmente, o valor médio de nível de cinza para o quadrado totalmente preenchido não é necessariamente 0 (pode ser maior); da mesma forma, o valor para o quadrado não preenchido não é necessariamente 255 (pode ser menor). O prof. João determinou que os quadrados seriam divididos em duas classes: aqueles com média menor ou igual a 127 serão considerados pretos e aqueles com média maior a 127 serão considerados brancos.

Obviamente, nem todas as questões das folhas de resposta são marcadas de maneira correta. Pode acontecer de um aluno se enganar e marcar mais de uma alternativa na mesma questão, ou não marcar nenhuma alternativa. Nesses casos, a resposta deve ser desconsiderada.

O professor João necessita agora de um voluntário para escrever um programa que, dados os valores dos cinco retângulos correspondentes às alternativas de uma questão determine qual a alternativa corretamente marcada, ou se a resposta à questão deve ser desconsiderada.
'''

alternativas = ('A', 'B', 'C', 'D', 'E')

def validarResposta(gabaritoDaQuestao):
    res = []
    if len(gabaritoDaQuestao) == 5:
        for alternativa in range(len(gabaritoDaQuestao)):
            if gabaritoDaQuestao[alternativa] <= 127:
                res.append(alternativa)

    return res[0] if len(res) == 1 else "*"



def gabaritoProva(n):
    gabarito = []
    for questao in range(n):
        res = input()
        res = res.split()
        list_res = list(map(int, res))
        gabarito.append(validarResposta(list_res))
    
    return gabarito


lista_gabaritos = []
while True:
    n = int(input())
    if n >= 1:
        res = gabaritoProva(n)
        lista_gabaritos.append(res)
    else: break

for i in lista_gabaritos:
    for j in i:
        if type(j) == int:
            print(alternativas[j])
        else:
            print(j)

#   font: BeeCrowd