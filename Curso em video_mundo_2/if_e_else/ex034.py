#Calculo de salário

funcionario = float(input('Informe o valor do seu salário: '))

if funcionario > 1250:
    aumento1 = funcionario + (funcionario * 0.10)
    print(f'{aumento1:.2f}')
else:
    aumento2 = funcionario + (funcionario * 15/100)
    print(f'{aumento2:.2f}')
