#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. seu aplicativo deverá analisar se a expressão
#passada está com os parênteses abertos e fechados na ordem correta


# cont = 0
# esq = 0
# direit = 0
# exp = list(input('Digite uma expresssão: '))
#
# for i, v in enumerate(exp):
#     if '(' in exp[i]:
#         cont += 1
#     if ')' in exp[i]:
#         cont -= 1
# if cont != 0:
#     print('Esta expressão está errada, verifique os parênteses!')
#
# else:
#     pala = ''.join(exp)
#     print(f'A expressão digitada foi: {pala} ')

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
