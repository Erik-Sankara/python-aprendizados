# crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. no final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

# alunos = list()
# media = 0
# nome = list()
# nota1 = []
# nota2 = []
# while True:
#     alunos.append(str(input('Digite o nome do aluno: ')))
#     while True:
#         nota1.append(int(input('digite a nota 1 do aluno: ')))
#         nota2.append(int(input('digite a nota 2 do aluno: ')))
#         cont = str(input('deseja continuar? [S/N]'))
#     nome.append(alunos, nota1, nota2)
#     if cont in 'nN':
#         break
# for c, v in enumerate(nome):
#     media =
#
# print(alunos)
# print(nome)
# print(media)

ficha = list()
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 30)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe):'))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')