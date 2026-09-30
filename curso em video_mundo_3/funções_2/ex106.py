#Sistema de ajuda

def ajuda():
    while True:
        print('\033[1;32;42m=-\033[m'* 15)
        print('\033[1;32;42m<<<SISTEMA DE AJUDA PyHELP>>>>\033[m')
        print('\033[1;32;42m=-\033[m'* 15)
        print('\033[m')

        sos = str(input('Função ou Biblioteca: ')).strip()

        print()

        if sos == 'fim':
            break
        else:
            print('\033[1;35;45m=-'* 20)
            print(f'\033[1;45m<<Acessando o manual do comando {sos}>>>')
            print('\033[1;35;45m=-\033[1;97m'* 20)
            help(sos)
            
ajuda()