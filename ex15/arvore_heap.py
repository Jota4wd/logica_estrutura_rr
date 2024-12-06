import os

def main():
    heap = Heap(31)
    heap.inserir(70)
    heap.inserir(40)
    heap.inserir(50)
    heap.inserir(20)
    heap.inserir(60)
    heap.inserir(100)
    heap.inserir(80)
    heap.inserir(30)
    heap.inserir(10)
    heap.inserir(90)

    while True:
        print("\nMenu:")
        print("1. Inserir elemento")
        print("2. Remover maior elemento")
        print("3. Mostrar heap")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            chave = int(input("Digite o valor a ser inserido: "))
            if heap.inserir(chave):
                print(f"Elemento {chave} inserido com sucesso.")
            else:
                print("Heap está cheio. Não foi possível inserir o elemento.")

        elif opcao == '2':
            maior = heap.remover_maior()
            if maior:
                print(f"Elemento removido: {maior.obtem_chave()}")
            else:
                print("Heap está vazio. Não há elementos para remover.")

        elif opcao == '3':
            heap.mostrar_heap()

        elif opcao == '4':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")


class Noh:
    def __init__(self, chave):
        self.chave = chave

    def obtem_chave(self):
        return self.chave

    def atribui_chave(self, nova_chave):
        self.chave = nova_chave


class Heap:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.tamanho_atual = 0
        self.matriz_heap = [None] * tamanho_maximo

    def esta_vazio(self):
        return self.tamanho_atual == 0

    def inserir(self, chave):
        if self.tamanho_atual == self.tamanho_maximo:
            return False
        novo_noh = Noh(chave)
        self.matriz_heap[self.tamanho_atual] = novo_noh
        self.borbulha_acima(self.tamanho_atual)
        self.tamanho_atual += 1
        return True

    def borbulha_acima(self, indice):
        pai = (indice - 1) // 2
        base = self.matriz_heap[indice]
        while indice > 0 and self.matriz_heap[pai].obtem_chave() < base.obtem_chave():
            self.matriz_heap[indice] = self.matriz_heap[pai]
            indice = pai
            pai = (pai - 1) // 2
        self.matriz_heap[indice] = base

    def remover_maior(self):
        if self.tamanho_atual == 0:
            return None
        raiz = self.matriz_heap[0]
        self.tamanho_atual -= 1
        self.matriz_heap[0] = self.matriz_heap[self.tamanho_atual]
        self.borbulha_abaixo(0)
        return raiz

    def borbulha_abaixo(self, indice):
        topo = self.matriz_heap[indice]
        while indice < self.tamanho_atual // 2:
            filho_esquerdo = 2 * indice + 1
            filho_direito = filho_esquerdo + 1
            if (filho_direito < self.tamanho_atual and
                    self.matriz_heap[filho_esquerdo].obtem_chave() < self.matriz_heap[filho_direito].obtem_chave()):
                filho_maior = filho_direito
            else:
                filho_maior = filho_esquerdo
            if topo.obtem_chave() >= self.matriz_heap[filho_maior].obtem_chave():
                break
            self.matriz_heap[indice] = self.matriz_heap[filho_maior]
            indice = filho_maior
        self.matriz_heap[indice] = topo

    def troca(self, indice, novo_valor):
        if indice < 0 or indice >= self.tamanho_atual:
            return False
        valorAntigo = self.matriz_heap[indice].obtem_chave()
        self.matriz_heap[indice].atribui_chave(novo_valor)
        if valorAntigo < novo_valor:
            self.borbulha_acima(indice)
        else:
            self.borbulha_abaixo(indice)
        return True

    def mostrar_heap(self):
        print('Conteúdo do Heap')
        for i in range(self.tamanho_atual):
            if self.matriz_heap[i] is not None:
                print(self.matriz_heap[i].obtem_chave(), end=' ')
            else:
                print('****', end=' ')
        print('\n' + '.' * 64)

        numeros_brancos = 32
        itens_linha = 1
        coluna = 0
        j = 0
        while self.tamanho_atual > 0:
            if coluna == 0:
                print(' ' * numeros_brancos, end='')

            print(self.matriz_heap[j].obtem_chave(), end=' ')
            j += 1
            if j == self.tamanho_atual:
                break

            coluna += 1
            if coluna == itens_linha:
                numeros_brancos //= 2
                itens_linha *= 2
                coluna = 0
                print()
            else:
                print(' ' * (numeros_brancos * 2 - 2), end='')

        print('\n' + '.' * 64)

if __name__ == "__main__":
    main()
