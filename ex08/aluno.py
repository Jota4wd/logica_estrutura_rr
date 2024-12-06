import os

def main():
    lista = []

    while True:
        os.system('clear')
        print('Opções:')
        print('<1> Cadastrar')
        print('<2> Consulta')
        print('<3> Sair')
        escolha = int(input(': '))

        if escolha == 1:
            os.system('clear')
            nome = input('Nome: ')
            endereco = input('Endereço: ')
            email = input('Email: ')

            obj = Aluno(nome, endereco, email)
            lista.append(obj)

        elif escolha == 2:
            for i in lista:
                print(i)
            input('\n\nEnter para continuar')

        elif escolha == 3:
            break


class Aluno:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email

    def __str__(self):
        return f'\nAluno: {self.nome}\nEndereço: {self.endereco}\nEmail: {self.email}'


if __name__ == '__main__':
    main()
