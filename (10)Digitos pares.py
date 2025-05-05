# Dado um array de numeros inteiros, retorne quantos deles contem um numero par de digitos.



# 1- Criar um array com numeros

numeros = ["1","4","56","16","612","612","5412","421","661","21312","11","5612","62"]

# 2- Converter o array para string

# string = str(numeros)   #nao funciona assim

# 3- Fazer um looping dentro do novo array para fazer a verificação de numeros com digitos pares
# 4- Fazer a contagem e mostrar na tela

contador = 0

for i in numeros:
    if len(i) % 2 == 0:
        contador += 1

print(contador)
    


    
