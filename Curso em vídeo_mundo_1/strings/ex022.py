#analisador de texto

nome = str(input('Digite seu nome completo: ')).strip()

maiuscula = nome.upper()
minuscula = nome.lower()
conta = (len(nome) - nome.count(' '))
primeiro = nome.find(' ')

print(f'Seu nome em letras maiusculas é: {maiuscula}')
print(f'Seu nome em letras minusculas é: {minuscula}')
print(f'Seu nome tem {conta} letras')
print(f'Seu primeiro nome tem {primeiro} letras')

