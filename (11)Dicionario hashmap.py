# Você recebe um array de numeros inteiros
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array
# Retorne a soma de todos os elementos unicos do array

array = [1,2,3,4,5,6,6,3,1,2,613,613,12,5]


# 1- Criar uma estrutura de dados para encontrar a quantidade de cada valor

hashmap = {}

for i in array:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i] += 1


# 2- Encontrar quem são os valores que aparecem uma unica vez
# 3- Fazer a soma das chaves que aparecem apenas uma vez

soma_chaves = 0

for chave, valor in hashmap.items():
    if valor == 1:
        soma_chaves += chave

print(soma_chaves)






