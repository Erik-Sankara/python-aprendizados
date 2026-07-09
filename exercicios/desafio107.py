#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade().
#faça também um programa que importe esse módulo e use algumas dessas funções

def aumentar(n, aum):
    tot = n
    aum /= 100
    n *= aum
    return n + tot



def diminuir(n, di):
    tot = n
    di /= 100
    n *= di
    return tot - n



def dobro(n):
    n *= 2
    return n



def metade(n):
    n /= 2
    return n


def moeda(n):
    return f"R${n:.2f}".replace('.',',')

