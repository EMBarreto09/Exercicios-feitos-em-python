#Dissecando uma váriavel

variavel = input('Digite algo: ')

print(type(variavel))
print(f'Só tem espaço? {variavel.isspace()}')
print(f'É um número? {variavel.isnumeric()}')
print(f'É alfabético? {variavel.isalpha()}')
print(f'Está em maiuscula? {variavel.isupper()}')
print(f'Está em minusculas? {variavel.islower()}')
print(f'Está capitalizada? {variavel.istitle()}')