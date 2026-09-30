#Cadastro de pessoas

pessoa = {}
pessoas = {}
cad = []

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['idade'] = int(input('Idade: '))
    pessoas['Cidade'] = str(input('Cidade: '))
    pessoas['Curso'] = str(input('Curso: '))

    cad.append(pessoas.copy())

    escolha = str(input('deseja continuar [s/n]: ')).strip().lower()[0]

    if escolha not in 'sn':
        escolha = str(input('ERRo, digite uma opção válida: ')).strip().lower()[0]
    if escolha in 'n':
        break

while True:
    print('-'*20)
    print("""MENU DE CADASTRO""")
    print("""1 - Cadastrar Pessoa
2 - Listar Pessoas
3 - Pesquisar pessoa
4 - Sair""")
    print('-'*20)

    menu = str(input('Qual opção deseja: '))

    if menu not in '1234':
        menu = int(input('ERRO, digite uma opção válida: '))
    if menu == '4':
        print('Fim Programa')
        break
    if menu == '3':
        busca = str(input('Digite o nome da pessoa que quer buscar: '))
        for p in cad:
            if busca in p['nome']:
                print(p)
    if menu == '2':
        print('='*35)
        for k, v in enumerate(cad):
            print(f'{k}:{v}')   
        print('='*50)
    if menu == '1':
        pessoa.clear()
        pessoa['nome'] = str(input('Nome: '))
        pessoa['idade'] = int(input('Idade: '))
        pessoa['Cidade'] = str(input('Cidade: '))
        pessoa['Curso'] = str(input('Curso: '))    
        cad.append(pessoa.copy())