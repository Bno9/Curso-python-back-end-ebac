# Receba um número e determine se ele é um palindromo (Lê-se igual de trás pra frente)

# 1- Receber um numero

numero = int(input())

# 2- Identificar se é um palindromo
# 3- Retornar se é ou nao

string = str(numero)
if string == string[::-1]:
    print("é um palindromo")
else:
    print("não é um palindromo")


