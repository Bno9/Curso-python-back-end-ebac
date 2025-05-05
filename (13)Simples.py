# Dado um array de numeros inteiros, retorne a soma do menor e do maior numero do array

# 1- Criar um array

array = [5521,512,612,717,836,261,91,45215,125]

# 2- Identificar o maior e o menor numero do array

array.sort()

# 3- Somar os valores e exibir na tela

primeiro_valor = array[0]
ultimo_valor = array[-1]

print(primeiro_valor + ultimo_valor)