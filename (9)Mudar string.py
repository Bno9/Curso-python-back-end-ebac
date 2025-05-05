# Dado um endereço IP válido (IPV4), retorne uma versão ajustada desse endereço IP.
# Um indereço IP ajustado substitui cada ponto "." por "[.]".


# 1- Receber a string com nosso endereço IP

ip = input()

# 2- Fazer a operação para substituir os pontos por parenteses e 

novo_ip = ""

for i in ip:
    if i == ".":
        novo_ip += "[.]"
    else:
        novo_ip += i


print(novo_ip)