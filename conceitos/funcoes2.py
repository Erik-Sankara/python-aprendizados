#INTERACTIVE HELP -- ir até o console do python e digitar help para saber mais informações 'help(<variável)'
#DOCSTRINGS -- """ manual do def para se ver no help()"""
#ARGUMENTOS OPCIONAIS -- não precisa dar todos os parâmetros, apenas incluir "=0" quando número
#ESCOPO DE VARIÁVEIS -- local onde uma variável vai existir ou não
#RETORNO DE RESULTADO -- funções podem retornar um valor ou não


# DOCSTRINGS + INTERACTIVE HELP
# def contador(i, f, p):
#     """
#     Faz uma contagem e mostra na tela
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='.. ')
#         c += p
#     print('FIM!')
#
#
# contador(0, 100, 10)
# help(contador)
#---------------------------------------------------------------------------------------------

# PARÂMETROS OPCIONAIS - aceita menos parâmetros delegados

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(3, 2, 5)
# somar(8, 4 )
# somar()
# somar(b=4, c=2)
#-----------------------------------------------------------------------------------------------

# ESCOPO GLOBAL -- mesmo "n" sendo declarado em baixo ve fora, o def em cima reconhece "n"
# ESCOPO LOCAL -- quando a variável é declarada apenas dentro do def
# é possível criar uma variável local e global
# escrever GLOBAl <variável> para usar a variável global
# def funcao():
#     global n1
#     print(f'N1 dentro vale {n1}')
#
# n1 = 2
# funcao()
# print(f'N1 global vale {n1}')
#-------------------------------------------------------------------------------------------------

#RETORNO DE VALORES -- o valor de "s" passa para a variável indicada

# def soma(a=0, b=0, c=0):
#     s = a + b + c
#     return s
# r1 = soma(3, 2, 5)
# r2 = (soma(2, 2))
# r3 = (6)
# print(f"Os resultados foram {r1}, {r2}, {r3}")
#-----------------------------------------------------------------------------------------------------------

def linha():
    print("-"*30)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1}, {f2} e {f3}")
linha()

def parouimpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("digite um número: "))
if parouimpar(num):
    print('É par!')
else:
    print("Não é par!")

