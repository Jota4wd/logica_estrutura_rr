from arvore import ArvoreBinaria

def menu():
    print("\nMenu:")
    print("0. Inserir valores aleatórios")
    print("1. Inserir um valor")
    print("2. Pesquisar um valor")
    print("3. Apagar um valor")
    print("4. Imprimir árvore")
    print("5. Imprimir árvore invertida")
    print("6. Tamanho da árvore")
    print("7. Profundidade máxima da árvore")
    print("8. Sair")

def main():
    arvore = ArvoreBinaria()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            quantidade = int(input("Digite a quantidade de valores a serem inseridos: "))
            min_valor = int(input("Digite o valor mínimo (ou Enter para usar 1): ") or "1")
            max_valor = int(input("Digite o valor máximo (ou Enter para usar 100): ") or "100")
            arvore.inserir_aleatorio(quantidade, min_valor, max_valor)
            print(f'{quantidade} valores aleatórios inseridos na árvore.')

        elif opcao == '1':
            valor = int(input("Digite o valor a ser inserido: "))
            arvore.raiz = arvore.insere(arvore.raiz, valor)
            print(f'Valor {valor} inserido na árvore.')

        elif opcao == '2':
            valor = int(input("Digite o valor a ser pesquisado: "))
            encontrado = arvore.pesquisa(arvore.raiz, valor)
            if encontrado:
                print(f'Valor {valor} encontrado na árvore.')
            else:
                print(f'Valor {valor} não encontrado na árvore.')

        elif opcao == '3':
            valor = int(input("Digite o valor a ser apagado: "))
            arvore.raiz = arvore.apaga(arvore.raiz, valor)
            print(f'Valor {valor} apagado da árvore.')

        elif opcao == '4':
            print("Árvore em ordem:")
            arvore.imprimirArvore(arvore.raiz)

        elif opcao == '5':
            print("Árvore invertida:")
            arvore.imprimeArvoreInvertida(arvore.raiz)

        elif opcao == '6':
            tamanho = arvore.tamanho(arvore.raiz)
            print(f'Tamanho da árvore: {tamanho}')

        elif opcao == '7':
            profundidade = arvore.profundidadeMaxima(arvore.raiz)
            print(f'Profundidade máxima da árvore: {profundidade}')

        elif opcao == '8':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()