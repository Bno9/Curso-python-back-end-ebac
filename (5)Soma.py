# Soma de 1 a N: Receba um número N e exiba a soma de todos os números de 1 até N.

# 1- Receba um numero aleatório

numero1 = int(input("Qual numero você quer somar?" ))

# 2- Exibir a soma de todos os numeros de 1 até esse numero

# numero2 = int(input("Até qual numero?" ))

soma = 0

for i in range (1, numero1 + 1):
    soma += i
    print("valor somado:")
    print(soma)
    print("numero atual:")
    print(i)



# for i in range(1, numero2 + 1):
    #print(numero1 + i)
