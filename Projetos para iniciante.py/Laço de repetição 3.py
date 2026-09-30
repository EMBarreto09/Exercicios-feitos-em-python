#verificador de senha

senha = "oi"
tentativa_senha = ""

while senha != tentativa_senha:
    tentativa_senha = input('Digite a senha: ')
    if tentativa_senha != senha:
        print('Errou!')
    else:
        print('Acertou!')