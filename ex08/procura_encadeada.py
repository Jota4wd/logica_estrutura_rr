import os

def main():
    primeiro = Aluno()
    atual = primeiro
    ultimo = primeiro

    while True:
        os.system('clear')
        print('Opções:')
        print('1 -> Cadastrar')
        print('2 -> Consultar')
        print('3 -> Pesquisar')
        print('4 -> Sair')
        escolha = input('Opção: ')

        if escolha == '1':
            os.system('clear')
            nome = input('Nome: ')
            endereco = input('Endereço: ')
            email = input('Email: ')

            obj = Aluno(nome, endereco, email)

            if primeiro.nome == '':
                primeiro = obj
                ultimo = primeiro
            else:
                ultimo.proximo = obj
                ultimo = ultimo.proximo

        elif escolha == '2':
            atual = primeiro
            while True:
                print(atual)
                if atual.proximo is None:
                    break
                else:
                    atual = atual.proximo

            input('Enter para continuar.')

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
    def __init__(self, nome='', endereco='', email=''):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.proximo = None


    def __str__(self):
        return f'\nAluno: {self.nome}\nEndereço: {self.endereco}\nEmail: {self.email}'


if __name__ == '__main__':
    main()
