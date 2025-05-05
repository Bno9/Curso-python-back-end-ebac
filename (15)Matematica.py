# Dado um array contendo n numeros distintos no intervalo [0, n]
# Retorne o unico numero no intervalo que está faltando no array

array = [0,1,3,4,5,6,7,8,9,10]

tamanho_array = len(array)
soma_valores = sum(array)
soma_total = tamanho_array * (tamanho_array + 1) / 2

print(soma_total - soma_valores)
print(tamanho_array)
print(soma_valores)