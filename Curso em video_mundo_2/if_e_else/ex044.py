#Gerenciador de pagamentos

escolha2 = 's'

while escolha2 == 's':
    print('=========== LOJAS GRAU MOGI ===========')
    print("")
    compra = float(input('Qual o valor da compra:R$ '))
    print("")
    print("""<<<[1] - à vista dinheiro/cheque>>>
<<<[2] - à vista no cartão>>>
<<<[3] - parcelado em 2x no cartão>>>
<<<[4] - parcelado em 3x ou mais no cartão>>>""")
    print("")
    escolha = input('<<<Digite a forma de pagamento>>> ')


    if escolha == '1':
        compra2 = compra - (compra * 10/100)
        print("")
        print(f'O valor da compra de R${compra:.2f} irá sair por {compra2:.2f} com 10% de desconto')
    elif escolha == '2':
        compra3 = compra - (compra * 5/100)
        print(f'Sua compra no valor de R${compra:.2f} irá sair por R${compra3:.2f} com seus 5% de desconto')
    elif escolha == '3':
        print(f'O valor final da compra será R${compra:.2f}')
    elif escolha == '4':
        input('Quantas vezes irá parcelar>>> ')
        compra4 = compra + (compra * 20/100)
        print(f'Sua compra que que era R${compra:.2f} com os juros do parcelamento irá sair por R${compra4:.2f}')
    print("")

    escolha2 = input('<<<Deseja algo mais>>> s ou n > ')

    if escolha2 != 's':
        print('Obrigado pela preferência, tenha um bom dia!')
        break
