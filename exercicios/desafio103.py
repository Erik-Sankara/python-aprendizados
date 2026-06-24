#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programador deverá ser capaz de mostrar a ficha de jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome='txt', gols=0):
    print(f"o jogador {nome} fez {gols} gols no campeonato!")

jogador = str(input("Digite o nome do jogador: "))
if jogador == "": jogador = "<Desconhecido>"
entrada = input("Digite quantos gols o jogador fez: ")
if entrada == "":
    feitos = 0

ficha(jogador, feitos)