#Média aritmética

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media > 6:
    print(f'A média da nota do aluno é de {media}')
    print(f'\033[1;32;40mPARABÉNS\033[m você passou') 
elif media < 5:
    print(f'A média da nota do aluno é de {media}')
    print(f'\033[1;31;40mREPROVADO\033[m')
else:
    print(f'A média da nota do aluno é de {media}')
    print(f'O aluno está de \033[1;34;40mRECUPERAÇÃO\033[m')