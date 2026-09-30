#Analise de expressão

expressao = str(input('Digite sua expressão: '))

verificador = expressao.count('(') + expressao.count(')')

if verificador % 2 == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')