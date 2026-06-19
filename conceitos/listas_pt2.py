''' LISTAS DENTRO DE LISTAS
lista dentro de listas:
dados = pedro, 25
pessoas = list
pessoas.append(dados[:])    -- cria uma cópia da lista dados

Criar de forma direta várias listas dentro de uma lista:
pessoas = [['pedro', 25], ['maria, 19], [joão, 32]  --pedro terá índice 0, maria 1 e joão 2

referênciar em uma lista composta:
print(pessoas[0][0]) = print(variável[<indice> da lista principal][<indice lista secundária>]

print(dados[0]) - mostra o dado indicado
'''

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])         #ao fazer um append(), cria uma ligação com as 2 estruturas, etão se não colocar como cópia, uma ação posterior pode contaminar a resposta
# print(galera)

# galera = [['joão', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1
print(f'há {totmai} maiores e {totmen} menores de idade')
