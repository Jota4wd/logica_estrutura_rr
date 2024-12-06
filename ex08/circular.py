import os

def main():
    lista = None
    ultimo = None

    while True:
        os.system('clear')
        print('Opções:')
        print('<1> Cadastrar')
        print('<2> Consultar')
        print('3 -> Pesquisar')
        print('4 -> Sair')
        escolha = int(input(': '))

        if escolha == 1:
            os.system('clear')
            nome = input('Nome: ')
            endereco = input('Endereço: ')
            email = input('Email: ')

            obj = Aluno(nome, endereco, email)
            if not lista:
                lista = obj
                ultimo = obj
                obj.proximo = obj
                obj.anterior = obj
            else:
                obj.anterior = ultimo
                obj.proximo = lista
                lista.anterior = obj
                ultimo.proximo = obj
                ultimo = obj

        elif escolha == 2:
            if not lista:
                print("Lista vazia.")
            else:
                current = lista
                while True:
                    print(current)
                    current = current.proximo
                    if current == lista:
                        break
            input('\n\nPressione Enter para continuar')

        elif escolha == '3':
            atual = primeiro
            nome = input('Nome: ')
            while True:
                if nome == atual.nome:
                    print(atual)
                if atual.proximo is None:
                    break
                else:
                    atual = atual.proximo

            input('Enter para continuar.')

        elif escolha == '4':
            break


class Aluno:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f'\nAluno: {self.nome}\nEndereço: {self.endereco}\nEmail: {self.email}'


if __name__ == '__main__':
    main()
