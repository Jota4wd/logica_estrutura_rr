import os

nome = None

while True:
    os.system('clear')
    print('Escolha uma opção: ')
    print('<1> -> Criar arquivo')
    print('<2> -> Escrever dados')
    print('<3> -> Listar conteúdo')
    print('<4> -> Fechar arquivo')
    print('<0> -> Sair')

    escolha = input('Enter: ')

    if escolha == '1':
        os.system('clear')
        nome = input('Nome do arquivo: ')
        if nome:
            with open(nome, 'w') as arquivo:
                print(f'Arquivo "{nome}" criado com sucesso.')

    elif escolha == '2':
        if nome is None:
            print('Primeiro crie o arquivo.')
            input('Enter: ')
        else:
            string = input('Digite o texto: \n')
            with open(nome, 'a') as arquivo:  # Usando 'a' para append
                arquivo.write(string + '\n')  # Adiciona uma nova linha após o texto

    elif escolha == '3':
        if nome is None:
            print('Primeiro crie o arquivo.')
            input('Enter: ')
        else:
            with open(nome, 'r') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)

            input('Enter: ')

    elif escolha == '4':
        if nome is None:
            print('Primeiro crie o arquivo.')
            input('Enter: ')
        else:
            print('Arquivo fechado.')
            nome = None  # Reseta o nome do arquivo

    elif escolha == '0':
        if nome is not None:
            print('Fechando arquivo...')
        break

    else:
        print('Siga o menu.')

print('Fim')
