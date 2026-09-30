#Área de um terreno

def terreno(l, c):
    area = l * c
    print(f'A área das dimensões {l} x {c} é igual a {area:.2f}')
def lin(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)

lin('Controle de terreno')
l = float(input('Qual a largura do terreno: '))
c = float(input('Qual o comprimento do terreno: '))
terreno(l, c)