#adapte o código do desafio 107, criando uma função adicional chamada moeda() que connsiga mostrar os valores como um valor monetário formatado
import desafio107
m = float(input("Digite o preço: R$"))

print(f"A metade de {desafio107.moeda(m)} é: {desafio107.moeda(desafio107.metade(m))}")
print(f"O dobro de {desafio107.moeda(m)} é: {desafio107.moeda(desafio107.dobro(m))}")
print(f"Aumentando 10%, temos: {desafio107.moeda(desafio107.aumentar(m, 10))}")
print(f"Reduzindo 13%, temos: {desafio107.moeda(desafio107.diminuir(m, 13))}")
