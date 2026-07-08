#Crie um programa que tenha a função leiaInt(), que vai funcionar semelhante à função input, so que fazendo a validação
# para aceitar apenas um valor numérico. EX.: n = leiaInt("Digite o numero: ")
def linha():
    print("-" * 30)
    print("versão do professor: ")
    print("-" * 30)
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido\033[m")
        if ok:
            break
    return valor


n = leiaint("digite um número: ")
print(f'Você acabou de digitar o número {n}')