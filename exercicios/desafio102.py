#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro o que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
def linha(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
linha("meu código: ")
def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        print(f, end=', ')
    if show == True:
        return f"O fatorial de {num} é: {f}"
    else:
        return f

f1 = int(input("digite um número: "))
f2 = str(input("deseja mostrar o resultado? [S/N]: ")).upper()
if 'S' in f2:
    f2 = True
else:
    f2 = False
print(fatorial(f2))

linha("código do professor: ")

def fatorial1(n,  show=False):
    """
    -> Calcula o fatorial de um número
    :param n: Um número a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: o valor do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
             print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial1(5, show=True))
help(fatorial1)