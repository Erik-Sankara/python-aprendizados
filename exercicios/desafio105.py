#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função
#
# def notas(lst):
#     pos = 0
#     while
def linha():
    print("-" * 30)
    print("resposta do professor: ")
    print("-" * 30)
def minha_resposta():
    def entrada(opc=False):
        """

        :param opc: Mostra a situação da turma com base na média "6"
        :return: Maior nota, menor nota, média da turma e situação <opcional>
        """
        c = 1
        maior = menor = 0
        media = 0
        sit = ""
        while True:
            usu = str(input("Deseja adicionar um número: [S/N] ")).upper()
            if usu != "S":
                break
            valor = int(input("Digite a nota: "))
            num[f"nota {c}"] = valor
            if c == 1:
                maior = menor = valor
            if valor >= maior:
                maior = valor
            elif valor <= menor:
                menor = valor
            media += valor
            c += 1
        media /= c
        if opc:
            if media < 6:
                sit = "RUIM"
            elif media >= 6:
                sit = "BOA!"
        else:
            sit = "<Não optante>"
        print(f"As notas digitadas foram: {num}")
        print(f"A maior nota é: {maior}, e a menor nota é: {menor}. A média da turma é: {media} e com isso a situação é: {sit}")

    num = {}
    entrada(opc=True)

linha()
def resposta_prof():
    def notas(*n, sit=False):
        """
        -> Função para analisar notas
        :param n: notas
        :param sit: situação <opcional>
        :return: total, média, maior, menor, situação
        """
        r = dict()
        r['total'] = len(n)
        r['maior'] = max(n)
        r['menor'] = min(n)
        r['media'] = sum(n)/len(n)
        if sit:
            if r['media'] >= 7:
                r['situação'] = 'BOA'
            elif r['media'] >= 5:
                r['situação'] = 'RASOÁVEL'
            else:
                r['situação'] = 'RUIM'
        return r

    resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
    print(resp)
    help(notas)
resposta_prof()
