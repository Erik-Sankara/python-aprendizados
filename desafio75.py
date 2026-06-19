#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre
#a - quantas vezes apareceu o valor 9
#b - em que posição foi digitado o promeiro valor 3
#c - Quais foram os números pares
t = ()
c = 0
par = ()

while c <= 3:
    valor = int(input('Digite um valor: '))
    t += (valor,)
    if valor % 2 == 0:
        par += (valor, )
    c += 1

print(t)
if 3 in t:
    print(t.index(3))
else:
    print('Não há números 3!')
print(t.count(9))
print(f'Os números pares são: {par if par else "não há pares"}')