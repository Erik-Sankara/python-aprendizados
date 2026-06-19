#faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre:
#A) quantas pessoas foram cadastradas
#B) uma listagem com as pessoas mais pesadas
#) uma listagem com as pessoas mais leves

leve = list()
usu: list()
pescad = 0
lista = list()
nomePeso = list()
#
while True:
    lista.append(str(input('Digite o nome da pessoa: ')))
    lista.append(int(input('Digite o peso da pessoa: ')))
    pescad += 1
    usu = str(input('Deseja inserir mais dados? [S/N] '))
    if usu in 'Nn':
        break
    
for i, v in enumerate(lista):
    if i % 2 == 1:
        if v >= 90:
            nomePeso.append(lista[i - 1])
        else:
            leve.append(lista[i - 1])
print(f'{pescad} pessoas foram cadastradas.')
print(f'Estas são as pessoas mais pesadas: {nomePeso}')
print(f'Estas são as pessoas mais leves: {leve}')