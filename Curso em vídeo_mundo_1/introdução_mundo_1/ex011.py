#Pintando parede

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

dimensao = largura * altura
pintar = dimensao / 2

print(f'A parede tem uma dimensâo de {largura} X {altura} e\nserá necessario de {pintar} litros de tinta para pintar ela toda')