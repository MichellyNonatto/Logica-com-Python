'''Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.'''

nome = input().capitalize()
list_values = [float(input()) for i in range(2)]

def calc_salario(total_vendas):
    total_comissao = total_vendas*0.15
    return total_comissao

print(f"TOTAL = R$ {calc_salario(list_values[1])+list_values[0]:.2f}")


#   fonte: BeeCrowd