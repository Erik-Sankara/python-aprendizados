#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro o que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        print(f, end=', ')
    if show == True:
        return f"O fatorial de {num} é: {f}"
    else:
        return "programa encerrado"

f1 = int(input("digite um número: "))
f2 = str(input("deseja mostrar o resultado? [S/N]: ")).upper()
if 'S' in f2:
    f2 = True
else:
    f2 = False
print(fatorial(f1, f2))