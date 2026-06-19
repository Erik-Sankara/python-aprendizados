#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
import random
num = 0
lista = ()
x = 0
maior = 0
menor = 0
while x <= 5:
    num = random.randint(1, 100)
    if x == 0:
        menor = num
    lista += (num, )
    x += 1
    if num >= maior:
        maior = num
    if num < menor:
        menor = num

print(menor)
print(maior)
print(lista)