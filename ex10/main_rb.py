from arvore_rb import RedBlackTree

def main():
    rbt = RedBlackTree()

    while True:
        print("\nMenu:")
        print("1. Inserir")
        print("2. Pesquisar")
        print("3. Apagar")
        print("4. Exibir")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            data = int(input("Digite o valor a ser inserido: "))
            rbt.insert(data)
            print(f"{data} inserido com sucesso.")

        elif choice == '2':
            data = int(input("Digite o valor a ser pesquisado: "))
            result = rbt.search(data)
            if result:
                print(f"Nó encontrado: {result.data}")
            else:
                print("Nó não encontrado.")

        elif choice == '3':
            data = int(input("Digite o valor a ser apagado: "))
            rbt.delete(data)  # Chama a função de deleção

        elif choice == '4':
            print("Elementos na árvore em ordem:")
            rbt.display()

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
