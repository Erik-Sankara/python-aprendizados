# faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# no finla mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valor = []
mai = 0
men = 0
pos_maior = []
pos_menor = []
for c in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
    if c == 0:
        mai = men = valor[c]
    else:
        if valor[c] > mai:
            mai = valor[c]

        if valor[c] < men:
            men = valor[c]

print(f'Os valores digitados foram {valor}!')
print(f'O maior número digitado foi o {mai}, na posição: ', end='')
for i, v in enumerate(valor):
    if v == mai:
        print(f'{i} ... ', end='')
print()
print(f'O menor número foi o {men}, na posição: ', end='')
for i, v in enumerate(valor):
    if v == men:
        print(f'{i} ... ', end='')
