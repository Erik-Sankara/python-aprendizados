# faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. no final,
# mostre o conteúdo da estrutura na tela
# média: 7
# nome input:
# média:
# situação: aprovado/reprovado

aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = int(input('Digite a média do aluno: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'
print('-='*30)
for k, v in aluno.items():
    print(k,':', v)
