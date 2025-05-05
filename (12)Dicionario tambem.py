# Dado um array de numeros inteiros, cada elemento aparece duas vezes, exceto um. Encontre ele.



# 1- Criar o array
Array = [1,1,2,2,3,3,4,5,5,6,6]


# 2- Criar um dicionario para adicionar os valores do array
Hashmap = {}

# 3- Criar um loop para adicionar as chaves e valores
for i in Array:
    if i not in Hashmap:
        Hashmap[i] = 1
    else:
        Hashmap[i] += 1

# 4- Verificar qual valor aparece apenas umas vez
for chave, valor in Hashmap.items():
    if valor == 1:
        print(chave)

