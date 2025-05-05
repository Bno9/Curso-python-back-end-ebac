# -- Aprovado, reprovado ou recuperação:

# 1- Receber a nota do aluno

nota = float(input())

# 2- Fazer a operação e mostrar o resultado

if nota < 5:
    print("Reprovado")

elif nota >=5 and nota < 8:
    print("Média")

elif nota >= 8:
    print("Muito bem")