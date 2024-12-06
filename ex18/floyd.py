# floyd.py

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
        self.matriz_caminhos = [[None] * self.num_vertice_max for _ in range(self.num_vertice_max)]
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
        self.matriz_caminhos[inicio][fim] = fim
        self.matriz_caminhos[fim][inicio] = inicio

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

    def floyd_warshall(self):
        # Cria cópias das matrizes para não modificar as originais
        dist = [row[:] for row in self.matriz_adj]
        prox = [row[:] for row in self.matriz_caminhos]

        # Algoritmo de Floyd-Warshall
        for k in range(self.num_vertice):
            for i in range(self.num_vertice):
                for j in range(self.num_vertice):
                    if dist[i][k] != self.INFINITO and dist[k][j] != self.INFINITO:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            prox[i][j] = prox[i][k]

        return dist, prox

    def mostrar_todos_caminhos(self):
        print("\nMenores caminhos entre todos os pares de vértices:")
        dist, prox = self.floyd_warshall()

        for i in range(self.num_vertice):
            for j in range(self.num_vertice):
                if i != j:
                    if dist[i][j] == self.INFINITO:
                        print(f"Não existe caminho de {self.lista_vertice[i].rotulo} para {self.lista_vertice[j].rotulo}")
                    else:
                        caminho = self.reconstruir_caminho(i, j, prox)
                        caminho_str = " -> ".join(self.lista_vertice[v].rotulo for v in caminho)
                        print(f"{self.lista_vertice[i].rotulo} para {self.lista_vertice[j].rotulo}:")
                        print(f"Caminho: {caminho_str}")
                        print(f"Distância: {dist[i][j]}\n")

    def mostrar_caminho_especifico(self, origem_rotulo, destino_rotulo):
        origem = self.buscar_vertice(origem_rotulo)
        destino = self.buscar_vertice(destino_rotulo)

        if origem is None or destino is None:
            print("Vértices não encontrados!")
            return

        dist, prox = self.floyd_warshall()

        if dist[origem][destino] == self.INFINITO:
            print(f"\nNão existe caminho de {origem_rotulo} para {destino_rotulo}")
            return

        caminho = self.reconstruir_caminho(origem, destino, prox)
        caminho_str = " -> ".join(self.lista_vertice[v].rotulo for v in caminho)
        print(f"\nMenor caminho de {origem_rotulo} para {destino_rotulo}:")
        print(f"Caminho: {caminho_str}")
        print(f"Distância: {dist[origem][destino]}")

    def reconstruir_caminho(self, origem, destino, prox):
        if prox[origem][destino] is None:
            return []

        caminho = [origem]
        while origem != destino:
            origem = prox[origem][destino]
            caminho.append(origem)
        return caminho

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def menu():
    print("\n=== MENU - FLOYD-WARSHALL ===")
    print("1. Adicionar vértice")
    print("2. Adicionar arco")
    print("3. Mostrar vértices")
    print("4. Mostrar arcos")
    print("5. Mostrar todos os menores caminhos")
    print("6. Mostrar caminho específico")
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
            grafo.mostrar_todos_caminhos()

        elif opcao == '6':
            origem = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")
            grafo.mostrar_caminho_especifico(origem, destino)

        elif opcao == '0':
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")
        limpar_tela()

if __name__ == '__main__':
    main()
