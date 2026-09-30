#financiando uma casa

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos você irá pagar a casa: '))

prestacao_mensal = (12 * anos)
prestacao_casa = valor_casa / prestacao_mensal
valor_mensal = salario * 30/100

print(f'Você irá pagar R${prestacao_casa:.2f} por mês em {prestacao_mensal} meses')

if prestacao_casa <= valor_mensal:
    print('\033[1;32;40mEmpréstimo aceito\033[m')
else:
    print('\033[1;;31;40mEmpréstimo negado\033[m')
