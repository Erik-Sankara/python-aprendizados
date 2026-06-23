#crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições
from datetime import date

ano = date.today().year
def voto(data):
    idade = ano - usu
    print(f'sua idade é: {idade}')
    if idade < 16:
        print("Você NÃO pode votar!")
    elif 16 <= idade < 18 or idade >= 65:
        print("Seu voto é OPCIONAL!")
    else:
        print("Voto OBRIGATÓRIO")


usu = int(input("Digite o seu ano de nascimento: "))
voto(usu)