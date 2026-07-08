#crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições
from datetime import date
def linha(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
ano = date.today().year

linha("meu código:")
def voto1(data):
    idade1 = ano - usu
    print(f'sua idade é: {idade1}')
    if idade1 < 16:
        print("Você NÃO pode votar!")
    elif 16 <= idade1 < 18 or idade1 >= 65:
        print("Seu voto é OPCIONAL!")
    else:
        print("Voto OBRIGATÓRIO")


usu = int(input("Digite o seu ano de nascimento: "))
voto1(usu)

linha("código do professor:")

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: NÂO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))