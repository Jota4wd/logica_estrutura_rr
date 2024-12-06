import os
from typing import List, Optional

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.esta_na_arvore = False

class Eixo:
    def __init__(self, inicio, fim, distancia):
        self.vertice_origem = inicio
        self.vertice_destino = fim
        self.distancia = distancia

class ListaPrioridades:
    def __init__(self):
        self.lista_prioridades = []
        self.MAXIMO = 20

    def inserir_item(self, arco_inserir):
        self.lista_prioridades.append(arco_inserir)
        self.lista_prioridades.sort(key=lambda x: x.distancia)

    def remover_minimo(self):
        return self.lista_prioridades.pop(0) if self.lista_prioridades else None

    def remover_n(self, n):
        if 0 <= n < len(self.lista_prioridades):
            self.lista_prioridades.pop(n)

    def esta_vazia(self):
        return len(self.lista_prioridades) == 0

    def encontrar(self, vertice_destino):
        for i in range(len(self.lista_prioridades)):
            if self.lista_prioridades[i].vertice_destino == vertice_destino:
                return i
        return -1

class Grafo:
    def __init__(self):
        self.INFINITO = float('inf')
        self.num_vertice_max = 20
        self.num_vertice = 0
        self.lista_vertice = []
        self.matriz_adj = [[self.INFINITO] * self.num_vertice_max for _ in range(self.num_vertice_max)]
        for i in range(self.num_vertice_max):
            self.matriz_adj[i][i] = 0
        self.lista_p = ListaPrioridades()
        self.num_vertices_arvore = 0

    def adicionar_vertice(self, rotulo):
        if self.num_vertice >= self.num_vertice_max:
            print("Limite máximo de vértices atingido!")
            return False
        if self.buscar_vertice(rotulo) is not None:
            print(f"Vértice '{rotulo}' já existe!")
            return False
        self.lista_vertice.append(Vertice(rotulo))
        self.num_vertice += 1
        return True

    def buscar_vertice(self, rotulo) -> Optional[int]:
        for i, v in enumerate(self.lista_vertice):
            if v.rotulo == rotulo:
                return i
        return None

    def adicionar_arco(self, inicio, fim, peso):
        self.matriz_adj[inicio][fim] = peso
        self.matriz_adj[fim][inicio] = peso

    def mostrar_vertices(self):
        print("\nVértices no grafo:")
        for i, v in enumerate(self.lista_vertice):
            print(f"{i}: {v.rotulo}")

    def mostrar_arcos(self):
        print("\nArcos no grafo:")
        for i in range(self.num_vertice):
            for j in range(i + 1, self.num_vertice):
                if self.matriz_adj[i][j] != self.INFINITO:
                    print(f"{self.lista_vertice[i].rotulo} -> {self.lista_vertice[j].rotulo}: {self.matriz_adj[i][j]}")

    def mstw(self):
        print("\nÁrvore Geradora Mínima (Algoritmo de Prim):")
        self.vertice_atual = 0
        while self.num_vertices_arvore < self.num_vertice - 1:
            self.lista_vertice[self.vertice_atual].esta_na_arvore = True
            self.num_vertices_arvore += 1
            for i in range(self.num_vertice):
                if i == self.vertice_atual or self.lista_vertice[i].esta_na_arvore:
                    continue
                distancia = self.matriz_adj[self.vertice_atual][i]
                if distancia == self.INFINITO:
                    continue
                self.inserir_fila_p(i, distancia)
            if self.lista_p.esta_vazia():
                print('Grafo não conectado')
                return
            eixo = self.lista_p.remover_minimo()
            vertice_origem = self.vertice_atual
            self.vertice_atual = eixo.vertice_destino
            print(f'{self.lista_vertice[vertice_origem].rotulo} -> {self.lista_vertice[self.vertice_atual].rotulo} (peso: {eixo.distancia})')
        for vertice in self.lista_vertice:
            vertice.esta_na_arvore = False

    def menor_caminho(self, origem_rotulo, destino_rotulo):
        origem = self.buscar_vertice(origem_rotulo)
        destino = self.buscar_vertice(destino_rotulo)

        if origem is None or destino is None:
            print("Vértices não encontrados!")
            return

        distancias = [self.INFINITO] * self.num_vertice
        anteriores = [None] * self.num_vertice
        visitados = [False] * self.num_vertice

        distancias[origem] = 0

        for _ in range(self.num_vertice):
            min_dist = self.INFINITO
            u = -1

            for i in range(self.num_vertice):
                if not visitados[i] and distancias[i] < min_dist:
                    min_dist = distancias[i]
                    u = i

            if u == -1:
                break

            visitados[u] = True

            for v in range(self.num_vertice):
                if (not visitados[v] and
                    self.matriz_adj[u][v] != self.INFINITO and
                    distancias[u] + self.matriz_adj[u][v] < distancias[v]):
                    distancias[v] = distancias[u] + self.matriz_adj[u][v]
                    anteriores[v] = u

        if distancias[destino] == self.INFINITO:
            print(f"\nNão existe caminho de {origem_rotulo} para {destino_rotulo}")
            return

        # Reconstruir o caminho
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(self.lista_vertice[atual].rotulo)
            atual = anteriores[atual]

        print(f"\nMenor caminho de {origem_rotulo} para {destino_rotulo}:")
        print(" -> ".join(reversed(caminho)))
        print(f"Custo total: {distancias[destino]}")

    def inserir_fila_p(self, vert, dist):
        indice_fila = self.lista_p.encontrar(vert)
        if indice_fila != -1:
            eixo_temp = self.lista_p.lista_prioridades[indice_fila]
            if eixo_temp.distancia > dist:
                self.lista_p.remover_n(indice_fila)
                eixo = Eixo(self.vertice_atual, vert, dist)
                self.lista_p.inserir_item(eixo)
        else:
            eixo = Eixo(self.vertice_atual, vert, dist)
            self.lista_p.inserir_item(eixo)

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def menu():
    print("\n=== MENU ===")
    print("1. Adicionar vértice")
    print("2. Adicionar arco")
    print("3. Mostrar vértices")
    print("4. Mostrar arcos")
    print("5. Mostrar árvore geradora mínima")
    print("6. Encontrar menor caminho")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    limpar_tela()
    grafo = Grafo()

    while True:
        opcao = menu()

        if opcao == '1':
            rotulo = input("Digite o rótulo do vértice: ")
            grafo.adicionar_vertice(rotulo)

        elif opcao == '2':
            grafo.mostrar_vertices()
            origem = input("Digite o rótulo do vértice de origem: ")
            destino = input("Digite o rótulo do vértice de destino: ")

            origem_idx = grafo.buscar_vertice(origem)
            destino_idx = grafo.buscar_vertice(destino)

            if origem_idx is None or destino_idx is None:
                print("Vértices inválidos!")
                continue

            try:
                peso = float(input("Digite o peso do arco: "))
                grafo.adicionar_arco(origem_idx, destino_idx, peso)
            except ValueError:
                print("Peso inválido!")

        elif opcao == '3':
            grafo.mostrar_vertices()

        elif opcao == '4':
            grafo.mostrar_arcos()

        elif opcao == '5':
            grafo.mstw()

        elif opcao == '6':
            origem = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")
            grafo.menor_caminho(origem, destino)

        elif opcao == '0':
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")
        limpar_tela()

if __name__ == '__main__':
    main()
