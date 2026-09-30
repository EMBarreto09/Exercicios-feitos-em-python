#Média aritmética

nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print(f'Á média do aluno é {media}')

if media > 5:
    print(f'\033[1;32;40mParabéns você passou de ano\033[m!!!')
else:
    print(f'\033[1;31;40mVocê foi reprovado\033[m!!!')
