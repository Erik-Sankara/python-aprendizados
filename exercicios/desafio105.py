#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função
#
# def notas(lst):
#     pos = 0
#     while
def entrada(ent):
    while True:
        usu = str(input("Deseja adicionar um número: [S/N] ")).upper()
        if usu != "S":
            break
        valor = int(input("Digite a nota: "))
        num[f"nota {c}"] = valor
        c += 1
maior = menor = 0
c = 1
num = {}


for v in num.values():
    if v == 0:
        menor = num
    if v >= maior:
        maior = num
    elif v <= menor:
        menor = num


print(num)
print(maior, menor)