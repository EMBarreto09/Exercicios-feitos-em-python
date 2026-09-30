#Formar triângulos

reta1 = int(input('Digite o valor de valor de uma reta: '))
reta2 = int(input('Digite o valor de outra reta: '))
reta3 = int(input('Digite o valor de mais uma reta: '))

tri1 = reta1 < reta2 + reta3
tri2 = reta2 < reta1 + reta3
tri3 = reta3 < reta2 + reta1

if (tri1 and tri2 and tri3) == True:
    print('Você pode formar um triângulo com esses valores')
else:
    print('Você não pode criar um triângulo com esses valores')

