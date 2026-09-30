#Verificar de idade

idade = int(input('Digite a sua idade: '))
idade_min = 18

if idade >= idade_min:
    print('ACESSO LIBERADO')
else:
    print('ACESSO BLOQUEADO!!!')