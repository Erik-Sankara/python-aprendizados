#crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. no final, mostre os valores pares e ímpares em ordem crescente

valores = list()
par = list()
impar = list()

for i in range(0, 7):
    valores.append(int(input('Digite um dos 7 valores: ')))
    if valores[i] % 2 == 0:
        par.append(valores[i])
    else:
        impar.append(valores[i])

par.sort()
impar.sort()
print(f'Os númerps pares foram: {par}!')
print(f'os númerps ímpares foram: {impar}!')
