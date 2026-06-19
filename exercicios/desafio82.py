# crie um programa que vai ler vários números e  colocar em uma lista. Depois disso, crie 2 listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente ao final, mostre o conteúdo das 3 listas geradas

num = 0
lista = []
par = []
impar = []
perg = str(input('Deseja colocar um número? [S/N]: '))
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    perg = str(input('Deseja continuar? [S/N]: '))
    if perg in 'Nn':
        break

print(f'Os números digitados foram: {lista}')
print(f'Estes são os números pares: {par}')
print(f'Estes são os números impares: {impar}')

