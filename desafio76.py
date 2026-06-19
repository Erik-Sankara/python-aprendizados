#crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços, na sequência.
#no final, mostre uma listagem de preços, organizando os dados em forma tabular
produto = ('Arroz', 5.99, 'Feijão', 7.50, 'Leite', 4.20, 'Pão', 12.00, 'Carne', 25.90, 'Frango', 15.75, 'Ovos', 10.30, 'Queijo', 8.45)
valor = ()
for c in range(0, 15, 2):
    valor = produto
    print(f'{produto[c]} ...... {produto[c+1]}')