#crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
#a - apenas os 5 primeiros colocados
#os ultimos 4 colocados da tabela
#c - uma lista com os times em ordem alfabética.
#d - em que posição na tabela está o time do flamengo
tabela = "Flamengo", "Palmeiras", "Fluminense", "Ceará", "Cruzeiro", "Bragantino", "Vasco", "Juventude", "Mirassol", "Internacional", "Botafogo", "Fortaleza", "Santos", "Corinthians", "Vitória", "São Paulo", "Grêmio", "Bahia", "Atlético-MG", "Sport"
print(f'Estes são os primeiros 5 times: {tabela[:5]}')
print(f'Estes são os últimos 4 da tabela: {tabela[-4:]}')
print(f'estes são os times em ordem alfabética: tabela: {sorted(tabela)}')
print(f'O flamengo está na posição: {tabela.index('Flamengo')}')