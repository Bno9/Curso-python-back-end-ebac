# Receba uma lista de palavras e ordene-as em ordem alfabetica

# 1- Criar a lista vazia

array = []

# 2- Definir uma quantidade de palavras

#5 palavras

# 3- Criar a logica para receber essas palavras e adicionar dentro do array

#loop = 1
#while loop == 1:
#    palavra = input("Digite o que quer colocar na lista")
#    Opcao = int(input("Deseja adicionar outro item? 1 para sim, 2 para sair"))
#
#    if Opcao == 1:
#        adicionar_palavra = array.append(palavra)
#
#    elif Opcao == 2:
#         adicionar_palavra = array.append(palavra)
#        loop = 0

for i in range(1, 6):
    palavra = input()
    print("Palavra adicionada")
    array.append(palavra)


# 4- Ordenar a lista

array.sort()

# 5- Mostrar na tela

print(array[::-1]) # com o ::-1 fica de Z-A e não A-Z