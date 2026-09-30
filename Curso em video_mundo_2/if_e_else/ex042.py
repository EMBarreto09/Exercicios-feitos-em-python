#Formar triângulos

reta1 = int(input('Digite o valor de valor de uma reta: '))
reta2 = int(input('Digite o valor de outra reta: '))
reta3 = int(input('Digite o valor de mais uma reta: '))

tri1 = reta1 < reta2 + reta3
tri2 = reta2 < reta1 + reta3
tri3 = reta3 < reta2 + reta1

if (tri1 and tri2 and tri3) == True:
    print('Você pode formar um triângulo com essas medidas')
    if reta1 != reta2 and reta1 != reta3:
        print('É um triângulo \033[1;33mESCALENO\033[m')
    elif (reta1 == reta2 == reta3):
        print('É um triângulo \033[1;31mEQUILÁTERO\033[m')
    elif (reta1 == reta2 or reta1 == reta3) or (reta2 == reta3):
        print('É um triângulo \033[1;34mISÓSCELES\033[m')
else:
    print('Você não pode formar um triângulo com essas medidas')