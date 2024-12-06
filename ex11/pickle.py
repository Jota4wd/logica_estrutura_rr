import os
import pickle

nome = None
arquivo = None
obj = None

class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def imprime(self):
        print(self.nome)

while True:
    os.system('clear')
    print('Eescolha uma opção:')
    print('<1> -> criar arquivo')
    print('<2> -> criar objeto')
    print('<3> -> gravar objeto')
    print('<4> -> recuperar objeto')
    print('<5> -> fechar arquivo')
    print('<0> -> sair')

    escolha = input('enter: ')

    if escolha == '1':
        os.system('clear')
        nome = input('nome do arquivo: ')
        if nome != None:
            arquiovo = open(nome, w)

    elif escolha =='2':
        nome_u = input('nome do usuario: ')
        obj = Usuario(nome_u)

    elif escolha == '3':
        if nome == None:
            print('criar arquivo primeiro....')
            input('enter:')
        elif obj == None:
            print('criar objeto primeiro...')
            input('enter:')
        else:
            pickle.dump(obj.arquivo)

    elif escolha == '4':
        if nome == None:
            print('criar arquivo primeiro')
        else:
            arquivo.close()
            arquivo = open(nome, 'r')
            obj = pickle.load(arquivo)
            print('arquivo recuperado')
            obj.imprime()
        input('enter:')

    elif escolha == '5':
        if nome == None:
            print('criar arquivo primeiro')
            input('enter:')
        else:
            arquivo.close()
            print('arquivo fechado.')
            input('enter:')

    elif escolha == '0':
        print('saindo...')
        break

print('fim')           
