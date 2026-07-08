#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programador deverá ser capaz de mostrar a ficha de jogador, mesmo que algum dado não tenha sido informado corretamente
def linha(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
def ficha(nome, gols):
    if not nome:
        nome = '<desconhecido>'
    if not gols:
        gols = 0
    print(f"o jogador '{nome}' fez '{gols}' gols no campeonato!")


jogador = str(input("Digite o nome do jogador: "))
entrada = input("Digite quantos gols o jogador fez: ")

ficha(jogador, entrada)

linha("Versão professsor: ")

def ficha1(jog='<Desconhecido>', gol=0):
    print(f'o jogador {jog} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():           #Saber se o que foi digitado é realmente um número
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha1(gol=g)
else:
    ficha1(n, g)
