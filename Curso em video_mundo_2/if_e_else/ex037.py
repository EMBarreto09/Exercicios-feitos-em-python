#Conversor de números

numero = int(input('Digite um número inteiro qualquer: '))
print('1 - Binário  2 - Octal  3 - Hexadecimal')
escolha = input('Esscolha uma das opções acima: ')

if escolha == '1':
    print(f'O número {numero} convertido para binário é {bin(numero)[2:]}')
elif escolha == '2':
    print(f'O número {numero} convertido para Octal é {oct(numero)[2:]}')
elif escolha == '3':
    print(f'O número {numero} convertido para Hexadeciaml é {hex(numero)[2:]}')
else:
    print('Opção inválida')
