'''LISTAS = []
listas são mutáveis:
    lanche[3] = 'picolé'

para adicionar um novo elemento na lista:
    lanche.append('biscoito')

para adicionar em um espaço específico:
    lanche.insert(0, 'cachorro quente') - o que representava o 0 vira 1...

para apagar elementos: - vai ser reposicionado os índices: o 4 vira 3...
    del lanche[3]
    lanche.pop(3) - geralmente apaga o último elemento, mas pode-se passar um parâmetro
    lanche.remove('<nome do elemento a ser retirado>')

criar uma lista com range:
    valores = list(rang(4, 11)) - começa no 4 e vai até o 10

organiza os valores que foram postos de forma aleatória:
    valores = [8,2,5,4,9,3,0]
    valores.sort()

para transformar valores em ordem mas de forma reversa:
    valores.sort(reverse=True)

saber o tamanho da lista:
    len(valores)

for <indice>, <valor - variável virtual> in enumerate(<nome lista>, <opcional: start=0>): Serve para percorrer listas/tuplas/dicionários:
para cada índice correspondente ao valor, enumerando pela lista, opcionalmente começa por número 0


'''

'''num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('não encontrei o valor')
print(num)
print(f'esta lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!',)
print('cheguei ao final da lista')'''

a = [2, 3, 4, 7]
b = a[:]                        #cria uma cópia de a em b
b[2] = 8
print(a)
print(b)