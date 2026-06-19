# DICIONARIOS, ao invés de ser índice, os dados recebem características



dados = dict()
dados = {'nome':'pedro', 'idade':25}
print(dados['nome'])

# Criando um novo elemento:
dados['sexo'] ='m'

# remover elementos:
del dados['idade']

# elementos que estão caracterizando os valores são chamados de keys:
filme = {'titulo': 'star wars',
         'ano': 1977,
         'diretor': 'George lucas'
}

# valor != keys:
print(filme.values()) # mostra todos os valores dentro de 'filmes': star wars, 1977, ...
print(filme.keys()) #mostra: titulo, ano, diretor
print(filme.items()) #mostra tanto o valor quanto as keys

# Exemplo de valor(v) x keys(k) em for
for k, v in filme.items():
    print(f'o {k} é {v}')

# É possível criar um dicionário dentro de lista:
locadora = list()
locadora.append(filme) # locadora '0' é star wars...

# para mostrar de maneira formatada:
print(locadora[0]['ano'])

print('---------------------------------------------------')

pessoas = {'nome': 'gustavo', 'sexo': 'm', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
for k in pessoas.values():
    print(k)
del pessoas['sexo']
pessoas['nome'] = 'leandro' #muda o nome
pessoas['peso'] = 98.5 #adiciona o peso
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*30)

#criando dicionário dentro de lista:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf']) #Cria uma lista com os 2 elementos separados por uma virgula -- pode gerar problemas
print('-='*30)
del brasil
#fatiamento para evitar repetição de informação no for com o metodo .copy()
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# print(brasil) ou
for e in brasil:
    for key, valuer in e.items():
        print(f'o campo {key} tem valor {valuer}.')
# ou

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()