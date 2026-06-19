# Crie um programa onde 4 joguem um dado e tenham resultados aleatórios. guarde esses resultados em um dicionário.
# no final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
lista = []
jog1 = {'nome':'joao', 'dado': 0}
jog2 = {'nome':'fernanda', 'dado': 0}
jog3 = {'nome':'ari', 'dado': 0}
jog4 = {'nome':'martin', 'dado': 0}
mai = list()
nome_mai = list()
lista.append(jog1.copy())
lista.append(jog2.copy())
lista.append(jog3.copy())
lista.append(jog4.copy())
pri = 0
for c, i in enumerate(lista):
    dado = random.randint(1, 6)
    lista[c]['dado'] = dado
    mai.append(dado)
for c in range(0, 4):
    if mai[c] > pri:
        pri = mai[c]
for i in range (0, 4):
    if lista[i]['dado'] == pri:
        nome_mai.append(lista[i]['nome'])
for i, c in enumerate(lista):
    lista.sort(key=lambda lista: lista['dado'], reverse=True)


for e in lista:
    for k, v in e.items():
        print(f' {k} : {v}', end=' ')
        print()


