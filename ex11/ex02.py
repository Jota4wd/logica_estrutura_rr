import json
import os
from datetime import datetime

class SimpleDatabase:
    def __init__(self):
        self.data = {}
        self.filename = 'db_data.json'
        self.load_database()  # Carrega o banco de dados automaticamente se existir

    def insert(self, table, record):
        if table not in self.data:
            self.data[table] = []
        # Adiciona timestamp ao registro
        record['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data[table].append(record)
        self.save_database()  # Salva automaticamente após cada inserção

    def query(self, table):
        return self.data.get(table, [])

    def save_database(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def load_database(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.data = json.load(f)
        except Exception as e:
            print(f"Erro ao carregar: {e}")
            self.data = {}

def print_help():
    print("\nExemplos de como usar:")
    print("\n1. Para inserir um registro:")
    print('   Digite o nome da tabela (ex: "usuarios")')
    print('   Digite o registro no formato: {"nome": "João", "idade": 25}')
    print('\n2. Para consultar, digite apenas o nome da tabela')
    print('   Ex: "usuarios"')

def main():
    db = SimpleDatabase()

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('=== Banco de Dados Simples ===')
        print('<1> -> Inserir registro')
        print('<2> -> Consultar tabela')
        print('<3> -> Ver exemplos de uso')
        print('<0> -> Sair')

        escolha = input('\nEscolha uma opção: ')

        if escolha == '1':
            print("\n-- Inserção de Registro --")
            tabela = input('Nome da tabela: ').strip().lower()
            print('\nDigite os dados no formato JSON, por exemplo:')
            print('{"nome": "João", "idade": 25}')

            try:
                registro = input('\nDados: ').strip()
                dados = json.loads(registro)
                db.insert(tabela, dados)
                print('\nRegistro inserido com sucesso!')
            except json.JSONDecodeError:
                print('\nErro: Formato JSON inválido!')

            input('\nPressione Enter para continuar...')

        elif escolha == '2':
            print("\n-- Consulta de Registros --")
            tabela = input('Nome da tabela: ').strip().lower()
            registros = db.query(tabela)

            if registros:
                print("\nRegistros encontrados:")
                for i, reg in enumerate(registros, 1):
                    print(f"\n{i}.", json.dumps(reg, indent=2))
            else:
                print("\nNenhum registro encontrado nesta tabela.")

            input('\nPressione Enter para continuar...')

        elif escolha == '3':
            print_help()
            input('\nPressione Enter para continuar...')

        elif escolha == '0':
            print('\nSaindo...')
            break

        else:
            print('\nOpção inválida!')
            input('Pressione Enter para continuar...')

if __name__ == '__main__':
    main()
