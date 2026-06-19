# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# caso o número já exista lá dentro, ele não será adicionado. No final, serão exibídos todos os valores únicos digitados, em ordem crescente.

valores = []
usu = ''
while True:
    num= int(input('Digite um número para ser adicionado à lista: '))
    if num not in valores:
        valores.append(num)
        print('Valor bem adicionado!')
    else:
        print('Valor duplicado')
    usu = input('Deseja continuar? [s/n] ')
    if usu == 'n':
        break

valores.sort()
print(f'Os números digitados foram: {valores}')