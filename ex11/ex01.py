import json
import os
from typing import Optional, List

class Node:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key: int) -> None:
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node: Node, key: int) -> None:
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def inorder(self) -> List[int]:
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node: Optional[Node]) -> List[int]:
        if node is None:
            return []
        return self._inorder_rec(node.left) + [node.value] + self._inorder_rec(node.right)

    def preorder(self) -> List[int]:
        return self._preorder_rec(self.root)

    def _preorder_rec(self, node: Optional[Node]) -> List[int]:
        if node is None:
            return []
        return [node.value] + self._preorder_rec(node.left) + self._preorder_rec(node.right)

    def search(self, key: int) -> bool:
        return self._search_rec(self.root, key)

    def _search_rec(self, node: Optional[Node], key: int) -> bool:
        if node is None:
            return False
        if node.value == key:
            return True
        if key < node.value:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)

    def save_to_file(self, filename: str) -> None:
        data = {
            'values': self.inorder(),
            'structure': self.preorder()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.root = None  # Reset tree
                for value in data['values']:
                    self.insert(value)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")

def print_tree(tree: BinaryTree) -> None:
    values = tree.inorder()
    if not values:
        print("Árvore vazia!")
        return

    print("\nValores em ordem crescente:", values)
    print("Total de números na árvore:", len(values))
    if values:
        print("Menor valor:", min(values))
        print("Maior valor:", max(values))

def main():
    tree = BinaryTree()
    filename = 'arvore_binaria.json'

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('=== Árvore Binária de Busca ===')
        print('<1> -> Inserir valor')
        print('<2> -> Buscar valor')
        print('<3> -> Mostrar árvore')
        print('<4> -> Salvar árvore')
        print('<5> -> Carregar árvore')
        print('<0> -> Sair')

        try:
            escolha = input('\nEscolha uma opção: ').strip()

            if escolha == '1':
                try:
                    valor = int(input('\nDigite um valor inteiro: '))
                    tree.insert(valor)
                    print(f'\nValor {valor} inserido com sucesso!')
                except ValueError:
                    print("\nErro: Digite apenas números inteiros!")

            elif escolha == '2':
                try:
                    valor = int(input('\nDigite o valor a buscar: '))
                    if tree.search(valor):
                        print(f"\nValor {valor} encontrado na árvore!")
                    else:
                        print(f"\nValor {valor} não encontrado na árvore!")
                except ValueError:
                    print("\nErro: Digite apenas números inteiros!")

            elif escolha == '3':
                print_tree(tree)

            elif escolha == '4':
                tree.save_to_file(filename)
                print(f'\nÁrvore salva em "{filename}"')

            elif escolha == '5':
                tree.load_from_file(filename)
                print(f'\nÁrvore carregada de "{filename}"')
                print_tree(tree)

            elif escolha == '0':
                print('\nSaindo...')
                break

            else:
                print('\nOpção inválida!')

        except Exception as e:
            print(f"\nErro: {e}")

        input('\nPressione Enter para continuar...')

if __name__ == '__main__':
    main()
