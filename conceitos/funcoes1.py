# def mostralinha():
#     print('-'*30)
#
# mostralinha()
# print("fazendo o teste")
# mostralinha()

# def titulo(txt):                               #passando parâmetros
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)
#
# titulo('Primeiros passos')                     #nome da função + o que aparecerá. Pode ter mais de 2
# titulo('descobrindo novas maneiras')

# def soma(a, b):                                  #Estilizando
#     print(f'A = {a} e b = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#
# soma(4, 5)

# def contador(* num):
#     tam = len(num)
#     print(f"Recebi os valores {num} e são ao todo {tam} números")
#     # for valor in num:
#     #     print(f'{valor} ', end='')
#     # print('FIM')
# contador(2, 1, 7)
# contador(8,0)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

#EMPACOTAMENTO:
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5, 2)
soma(2, 9, 4)