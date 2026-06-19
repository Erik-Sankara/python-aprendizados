# crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre
#A) quantos números foram digitados
#B) A lista de valores, ordenada de forma decrescente
#C) Se o valor 5 foi digitado e está ou não na lista
cinco = ''
lista = []
numD = 0
resp = str(input('Você quer digitar um número? [S/N]: '))
while True:
    lista.append(int(input('Digite um número: ')))
    numD += 1
    resp = str(input('Você quer digitar um número? [S/N]'))
    if resp == 'n':
        break

for i, v in enumerate(lista):
    if lista[i] == 5:
        cinco = 'sim'


lista.sort(reverse=True)
print(f'Foram digitados {numD} números')
print(f'Estes são os valores {lista}')
print(f'Há algum número cinco na lista? {cinco}')