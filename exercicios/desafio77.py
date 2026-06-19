#crie um programa que tenha um tupla com várias palavras (não usar acento). depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

palavra = ("alegria", "esperança", "liberdade", "aventura", "serenidade", "foguete", "melodia", "abraço")
vogal = ('a', 'e', 'i', 'o', 'u')
vogal1 = ()
for c in range(0, 7):
    vogal1 = ()
    for v in range(0, 5):
        if vogal[v] in palavra[c]:
            vogal1 += (vogal[v], )
    print(f'{palavra[c]} .......  {vogal1}')
