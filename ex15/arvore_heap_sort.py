import os
import random

def main():
    os.system('clear')
    numero_itens = int(input('numero de itens: '))
    heap = Heap(numero_itens)
    for i in range(numero_itens):
        rng = random.randint(1, 100)
        novo_noh = Noh(rng)
        heap.inserir_em(i, novo_noh)
        heap.incrementar_tamanho()
    print('matriz aleatoria')
    heap.mostra_matriz()
    j = numero_itens // 2 - 1
    while j >= 0:
        heap.borbulha_abaixo(j)
        j -= 1
    heap.mostrar_heap()
    j = numero_itens - 1
    while j >= 0:
        maior_noh = heap.remover_maior()
        heap.inserir_em(j, maior_noh)
        j -= 1
    print('ordenada')
    heap.mostra_matriz()


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

    def inserir_em(self, indice, noh):
        self.matriz_heap[indice] = noh

    def mostra_matriz(self):
        for i in range(self.tamanho_maximo):
            print(self.matriz_heap[i].obtem_chave(), end=' ')
        print()

    def incrementar_tamanho(self):
        self.tamanho_atual += 1

if __name__ == "__main__":
    main()

