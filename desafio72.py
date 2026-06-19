#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
#seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso]

n = int(input('Digite um número entre 0 e 20: '))
numero = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"

while n > 20 or n < 0:
    print('Este número não é valido! Digite novamente')
    n = int(input('Digite um número entre 0 e 20: '))
print(numero[n])