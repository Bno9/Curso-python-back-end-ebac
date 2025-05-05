# Dado um array de inteiros, um inteiro sortudo é um inteiro que tem uma frequencia no array igual seu valor


# 1- Criar o array
array = [1,2,2,3,4,5,3,1,5,3,8,4]


# 2- Criar o hashmap
hashmap = {}

# 3- Usar o for para adicionar os valores no hashmap
for i in array:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i] += 1

# 4- Verificar quem é o inteiro sortudo e mostrar 
for chave, valor in hashmap.items():
    if chave == valor:
        print(chave)
        



#essa aula o professor deu uma motivação!