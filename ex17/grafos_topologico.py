import os

def main():
    os.system('clear')
    grf = Grafo()
    while True:
        print('Escolha a opção:')
        print('M -> mostrar, V -> inserir vértice, A -> inserir arco, T -> topologico,  S -> sair')
        escolha = input('-> ').lower()
        if escolha == 'm':
            grf.imprimir_matriz()
        elif escolha == 'v':
            val = input('Rótulo do vértice: ')
            grf.adicionar_vertice(val)
        elif escolha == 'a':
            r_inicio = input('Rótulo do vértice de início: ')
            inicio = grf.localizar_rotulo(r_inicio)
            if inicio == -1:
                print('Vértice não cadastrado')
                input()
                continue
            r_fim = input('Rótulo do vértice de fim: ')
            fim = grf.localizar_rotulo(r_fim)
            if fim == -1:
                print('Vértice de fim não cadastrado')
                input()
                continue
            grf.adicionar_arco(inicio, fim)
        elif escolha == 't':
            grf.topo()            
        elif escolha == 's':
            break
        else:
            print('Opção inválida')
            input()


class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False

    def igual_a(self, r):
        return r == self.rotulo

    def foi_visitado(self):
        return self.visitado

    def reg_visitado(self):
        self.visitado = True

    def limpa(self):
        self.visitado = False


class Grafo:
    def __init__(self):
        self.num_vertices_maximo = 20
        self.num_vertices = 0
        self.lista_vertices = []
        self.matriz_adj = [[0] * self.num_vertices_maximo for _ in range(self.num_vertices_maximo)]
        self.matriz_ordenada = []

    def adicionar_vertice(self, rotulo):
        if self.num_vertices < self.num_vertices_maximo:
            self.lista_vertices.append(Vertice(rotulo))
            self.num_vertices += 1
        else:
            print("Número máximo de vértices atingido.")

    def adicionar_arco(self, inicio, fim):
        if inicio < self.num_vertices and fim < self.num_vertices:
            self.matriz_adj[inicio][fim] = 1
        else:
            print("Índices de vértice inválidos.")

    def mostrar_vertice(self, vertice):
        print(self.lista_vertices[vertice].rotulo)

    def imprimir_matriz(self):
        print('Matriz de Adjacência:')
        print('  ', end='')
        for i in self.lista_vertices:
            print(i.rotulo, end=' ')
        print()
        for i in range(self.num_vertices):
            print(self.lista_vertices[i].rotulo, end=' ')
            for j in range(self.num_vertices):
                print(self.matriz_adj[i][j], end=' ')
            print()

    def localizar_rotulo(self, rotulo):
        for i in range(self.num_vertices):
            if self.lista_vertices[i].igual_a(rotulo):
                return i
        return -1

    def obtem_adj_nao_visitado(self, v):
        for i in range(self.num_vertices):
            if self.matriz_adj[v][i] == 1 and not self.lista_vertices[i].foi_visitado():
                return i
        return -1

    def topo(self):
        while self.num_vertices > 0:
            vertice_atual = self.obtem_sem_sucessor()
            if vertice_atual == -1:
                print('Erro: grafo com ciclos')
                return
            self.matriz_ordenada.append(self.lista_vertices[vertice_atual].rotulo)
            self.remove_vertice(vertice_atual)
        self.matriz_ordenada.reverse()
        print(f'Ordenada topologicamente: {self.matriz_ordenada}')

    def obtem_sem_sucessor(self):
        for linha in range(self.num_vertices):
            eh_eixo = False
            for coluna in range(self.num_vertices):
                if self.matriz_adj[linha][coluna] > 0:
                    eh_eixo = True
                    break
            if not eh_eixo:
                return linha
        return -1

    def remove_vertice(self, vertice):
        # Remove a linha correspondente do matriz_adj
        del self.matriz_adj[vertice]
        
        # Remove a coluna correspondente de todas as linhas restantes
        for linha in self.matriz_adj:
            del linha[vertice]
        
        # Remove o vértice da lista de vértices
        del self.lista_vertices[vertice]
        self.num_vertices -= 1


if __name__ == '__main__':
    main()