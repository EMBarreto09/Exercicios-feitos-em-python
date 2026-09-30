#Def, chamando funções

from math import sqrt

continuar = 's'

while continuar == 's':
    def somar(n1, n2):
        resultado = n1 + n2
        print(f'O resultado de {n1} + {n2} é {resultado}')

    def multiplicar(n1, n2):
        resultado = n1 * n2
        print(f'O resultado de {n1} x {n2} é {resultado}')

    def subtrair(n1, n2):
        resultado = n1 - n2
        print(f'O resultado de {n1} - {n2} é {resultado}')

    def dividir(n1, n2):
        resultado = n1 / n2
        print(f' {n1} / {n2} é {resultado:.2f}')

    def potencia(n1, n2):
        resultado = n1 ** n2
        print(f'O resulatado de {n1} elevado a {n2} é {resultado}') 

    def raiz(n1):
        resultado = sqrt(n1)
        print(f'A raiz quadrado de {n1} é {resultado:.2f}')

    print('-----------------------------------------------------------------------')
    print('1-soma', '2-Multiplicação', '3-Subtração', '4-Divisão', '5-Potência', '6-Raiz quadrada')
    print('-----------------------------------------------------------------------')
    escolha = input('Digite o número da operação que irá escolher: ')

    if escolha == '6':
        n1 = int(input('Digite um número para ver a sua raiz: '))
    else:
        print(f'Você escolheu a operação {escolha}')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

    if escolha == '1':
        resultado = somar(n1, n2)
    elif escolha == '2':
        resultado = multiplicar(n1, n2)
    elif escolha == '3':
        resultado = subtrair(n1, n2)
    elif escolha == '4':
        resultado = dividir(n1, n2)
    elif escolha == '5':
        resultado = potencia(n1, n2)
    elif escolha == '6':
        resultado = raiz(n1)
    else:
        print('Opção não encontrada')

    continuar = input('<<< Deseja realizar outra conta?: s ou n >>> ')

    if continuar != 's':
        break

print('Fim do programa :)')