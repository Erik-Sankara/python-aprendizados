#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista.
#Já na posição correta de inserção (sem usar sort). No final, mostre a lista ordenada na tela

# num = []
# posi = 0
# ordem = []
# for i in range(0, 5):
#     num.append(int(input(f'Digite um número: ')))
#     if i == 0:
#         posi = num[0]
#     elif num[i] <= posi:
#         ordem.insert(0, num)
# print(ordem)
# print(num)

lista =[]
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)             #este manda o número para o final, então é usado para comparar com o último valor
    else:
        pos = 0
        while pos < len(lista):         #percorre toda a lista e salva a posiçãp da lista no pos, para saber onde inserir depois
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print(lista)