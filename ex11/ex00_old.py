import os

nome = None
arquivo = None

while True:
    os.system('clear')
    print('escolha uma opção: ')
    print('<1> -> criar arquivo')
    print('<2> -> escrever dados')
    print('<3> -> listar conteudo')
    print('<4> -> fechar arquivo')
    print('<0> -> sair')

    escolha = input('enter: ')

    if escolha == '1':
        os.system('clear')
        nome = input('nome do arquivo: ')
        if nome != None:
            arquivo = open(nome, 'w')

    elif escolha == '2':
        if nome == None:
            print('primeiro crie o arquivo')
            input('enter: ')
        else:
            string = input('digite o texto: \n')
            arquivo.write(str(string))

    elif escolha == '3':
        if nome == None:
            print('primeiro crie o arquivo')
            input('enter: ')
        else:
            arquivo.close()
            arquivo = open(nome, 'r')
            for line in arquivo:
                print(line)
            arquivo.close()
            arquivo = open(nome, 'a')
            input('enter: ')

    elif escolha == '4':
        if nome == None:
            print('primeiro cire o arquivo')
            input('enter: ')
        else:
            arquivo.close()
            print('fechando...')
            input('enter: ')

    elif escolha == '0':
        arquivo.close()
        break

    else:
        print('siga o menu: ')


print('fim')
