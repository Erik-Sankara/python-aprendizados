'''TUPLAS
variável composta
pode ser posta entre parenteses ou sem
os elementos dentro dela são identificados por números a partir do 0
ex de fatiamento:
    lanche = hamburguer, suco, pizza, pudim
    print(lanche[2])
    resultado: pizza
    print(lanche[0:2] - pega os elementos do 0 até o 1, pois ignora o último
    resultado: hamburguer, suco
    print(lanche[1:]
    resultado: suco, pizza, pudim
    print(lanche[-1]) - acessa o lanche de forma contrária
    resultado: pudim

    len(lanche) - quantos elementos tem dentro de lanche
    resultado: 4

    for c in lanche: - estrutura de repetição. repete até todos os elementos passarem no print
        print(c)
    resultado: hamburger - suco - ...
LIMITAÇÂO: as tuplas são imutáveis
'''


#lanche = ('hamb', 'suco', 'pizza', 'pudim')
#for c in range(0, len(lanche)):
#    print(f'eu vou comer {lanche[c]}')

#for c in lanche:
#    print(f'eu vou comer {c}')

#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')


#print(sorted(lanche)) #mostra a variavel em ordem

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a #junta as tuplas - não soma'''
#print(len(c))
#print(c.count(5)) - quantas vezes aparece o número 5
#print(c)
#print(c.index(8)) - em qual posição está o 8
#print(c.index(5, 1)) - começa na posição 1 e procura onde está o 5

pessoa = 'gustavo', 39, 'M', 99.88
del(pessoa)
print(pessoa)