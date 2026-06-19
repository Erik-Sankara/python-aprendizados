#faça um programa que ajude um jogador da mega-sena a criar palpites. o programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
import random
jogos = []
usu = []
perg = int(input('Quantos jogos você deseja fazer? '))

for i in range(perg):
    jogos = [random.randint(1, 60) for i in range(6)]
    usu.append(jogos)


for c, v in enumerate(usu):
    print(f'O {c+1}º jogo é: {usu[c]}')