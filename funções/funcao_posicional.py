# def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#     print(modelo, ano, placa, motor, combustivel)

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat", motor="1.0" combustivel="Gasolina") # invalido - obrigatoriamente antes da / é somente a entrada do valor, não é trabalho com o nome do parâmetro.

# def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)

# criar_carro2(modelo="Palio", ano="1999", placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido


# criar_carro2("Palio", "1999", "ABC-123", "Fiat", "1.0", "Gasolina") # inválido - todos os parâmetros após o * é obrigatório distribuir os parâmetros com a palavra chave correspondente.

# objetos de primeira classe - quando uma função manipula o resultado de outra função


funcao_lambda = lambda list, funcao:print(f"O resultado da operação {list[0]} + {list[1]} = {funcao(list)}")
funcao_lambda([5, 8], sum)
