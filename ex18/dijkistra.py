# dijkstra.py

import os
from typing import Optional

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo

class Grafo:
    def __init__(self):
        self.INFINITO = float('inf')
        self.num_vertice_max = 20
        self.num_vertice = 0
        self.lista_vertice = []
        self.matriz_adj = [[self.INFINITO] * self.num_vertice_max for _ in range(self.num_vertice_max)]
        for i in range(self.num_vertice_max):
            self.matriz_adj[i][i] = 0

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

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def menu():
    print("\n=== MENU - MENOR CAMINHO (DIJKSTRA) ===")
    print("1. Adicionar vértice")
    print("2. Adicionar arco")
    print("3. Mostrar vértices")
    print("4. Mostrar arcos")
    print("5. Encontrar menor caminho")
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
