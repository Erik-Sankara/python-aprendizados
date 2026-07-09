# Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário
# digitar a palavra 'FIM', o programa se encerrará.
# obs: Use cores

def minha_resposta():
    def sistema(a=str):
        azul = "\033[1;30;44m"
        reset = "\033[m"
        linha = f"{azul}-{reset}" * 24
        print(linha)
        print(f"{azul}SISTEMA DE AJUDA PyHELP {reset}")
        print(linha)
        while True:
            usu = str(input('Qual comando ou bibliotéca você deseja descobrir? '))
            help(usu)
            print("\033[1;31;43m-\033[m" * 24)
            fim = str(input("\033[1;31;43mDeseja continuar? [S/N] \033[m")).upper()
            print("\033[1;31;43m-\033[m" * 24)
            if fim == "N":
                print(linha)
                print(f"\033[1;30;44mSISTEMA FINALIZADO!     {reset}")
                print(linha)
                break


def resposta_professor():
    from time import sleep
    c = ('\033[0m',          #0 - sem cor
         '\033[0;30;41m',    #1 - vermelho
         '\033[0;30;42m',    #2 - verde
         '\033[0;30;43m',    #3 - amarelo
         '\033[0;30;44m',    #4 - azul
         '\033[0;30;45m',    #5 - roxo
         '\033[0;30m'        #6 - branco
         );

    def ajuda(com):
        titulo(f'Acessando o manual do comando \'{com}\'', 4)
        print(c[6], end='')
        help(com)
        print(c[0], end='')
        sleep(2)

    def titulo(msg, cor=0):
        tam = len(msg) +4
        print(c[cor], end='')
        print('~' * tam)
        print(f'  {msg}')
        print('~' * tam)
        print(c[0], end='')
        sleep(1)


    # Programa principal
    comando = ''
    while True:
        titulo("SISTEMA DE AJUDA PyHELP", 2)
        comando = str(input("Função ou Biblioteca > "))
        if comando.upper() == "FIM":
            break
        else:
            ajuda(comando)
    titulo("ATÉ LOGO", 1)
resposta_professor()