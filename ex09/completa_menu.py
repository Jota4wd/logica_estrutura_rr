from completa import ArvoreBinaria
import random

def exibir_menu():
    print("\n=== Menu da Árvore Binária ===")
    print("1. Inserir valores aleatórios")
    print("2. Inserir valor")
    print("3. Remover valor")
    print("4. Pesquisar valor")
    print("5. Imprimir árvore visual")
    print("6. Mostrar travessias")
    print("7. Informações da árvore")
    print("8. Limpar árvore")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    arvore = ArvoreBinaria()
    
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            quantidade = int(input("Digite a quantidade de valores a serem inseridos: "))
            min_valor = int(input("Digite o valor mínimo (ou Enter para usar 1): ") or "1")
            max_valor = int(input("Digite o valor máximo (ou Enter para usar 100): ") or "100")

            # Conjunto para armazenar valores únicos
            valores_inseridos = set()

            while len(valores_inseridos) < quantidade:
                # Gere um valor aleatório
                valor_aleatorio = random.randint(min_valor, max_valor)
                
                # Verifique se o valor já foi inserido
                if valor_aleatorio not in valores_inseridos:
                    arvore.raiz = arvore.insere(arvore.raiz, valor_aleatorio)  # Passando a raiz como argumento
                    valores_inseridos.add(valor_aleatorio)

            print(f'{len(valores_inseridos)} valores únicos inseridos na árvore.')

        elif opcao == "2":
            try:
                valor = int(input("Digite o valor a ser inserido: "))
                arvore.raiz = arvore.insere(arvore.raiz, valor)
                print(f"Valor {valor} inserido com sucesso!")
            except ValueError:
                print("Por favor, digite um número válido.")
        
        elif opcao == "3":
            if arvore.raiz is None:
                print("Árvore vazia!")
                continue
            try:
                valor = int(input("Digite o valor a ser removido: "))
                arvore.raiz = arvore.apaga(arvore.raiz, valor)
                print(f"Valor {valor} removido com sucesso!")
            except ValueError:
                print("Por favor, digite um número válido.")
        
        elif opcao == "4":
            if arvore.raiz is None:
                print("Árvore vazia!")
                continue
            try:
                valor = int(input("Digite o valor a ser pesquisado: "))
                noh = arvore.pesquisa(arvore.raiz, valor)
                if noh:
                    print(f"Valor {valor} encontrado!")
                    print(f"Filho esquerdo: {noh.esquerdo.dado if noh.esquerdo else 'None'}")
                    print(f"Filho direito: {noh.direito.dado if noh.direito else 'None'}")
                else:
                    print(f"Valor {valor} não encontrado!")
            except ValueError:
                print("Por favor, digite um número válido.")
        
        elif opcao == "5":
            if arvore.raiz is None:
                print("Árvore vazia!")
                continue
            print("\nEstrutura da árvore:")
            arvore.imprimirArvoreVisual(arvore.raiz)
        
        elif opcao == "6":
            if arvore.raiz is None:
                print("Árvore vazia!")
                continue
            print("\nTravessias:")
            print("Pre-ordem:", end=" ")
            arvore.travessiaPreOrdem(arvore.raiz)
            print("\nEm-ordem:", end=" ")
            arvore.travessiaEmOrdem(arvore.raiz)
            print("\nPos-ordem:", end=" ")
            arvore.travessiaPosOrdem(arvore.raiz)
            print("\nPor nível:")
            arvore.travessiaPorNivel(arvore.raiz)
        
        elif opcao == "7":
            if arvore.raiz is None:
                print("Árvore vazia!")
                continue
            print("\nInformações da árvore:")
            print(f"Altura: {arvore.getAltura(arvore.raiz)}")
            print(f"Número de nós: {arvore.tamanho(arvore.raiz)}")
            print(f"Menor valor: {arvore.menorValor(arvore.raiz).dado}")
            print(f"Maior valor: {arvore.maiorValor(arvore.raiz).dado}")
            print(f"É uma BST válida? {arvore.ehBST(arvore.raiz)}")
        
        elif opcao == "8":
            arvore = ArvoreBinaria()
            print("Árvore limpa com sucesso!")
        
        elif opcao == "0":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()