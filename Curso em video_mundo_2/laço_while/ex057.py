#Verificador de sexo

sexo = str(input("Sexo [M/F]: ")).strip().lower()[0]

while sexo not in 'mf':
    print('Dados inválidos. Tente novamente')
    sexo = str(input('informe o sexo [M/F]: ')).strip().lower()[0]
if sexo in 'mf':
    if sexo == 'm':
        print('Sexo registrado [Masculino]')
    elif sexo == 'f':
        print('Sexo registrado [Feminino]')