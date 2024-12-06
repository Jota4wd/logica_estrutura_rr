import os

def main():
    os.system('clear')
    grf = Grafo()
    while True:
        print('Escolha a opção:')
        print('M -> mostrar, V -> inserir vértice, A -> inserir arco, W -> warshall, S -> sair')
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
        elif escolha == 'w':
            grf.warshall()
        elif escolha == 's':
            break
        else:
            print('Opção inválida')
            input()

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo

    def igual_a(self, r):
        return r == self.rotulo

class Grafo:
    def __init__(self):
        self.num_vertices_maximo = 20
        self.num_vertices = 0
        self.lista_vertices = []
        self.matriz_adj = []
        for i in range(self.num_vertices_maximo):
            linha_matriz = [0] * self.num_vertices_maximo
            self.matriz_adj.append(linha_matriz)

    def adicionar_vertice(self, rotulo):
        if self.num_vertices < self.num_vertices_maximo:
            self.lista_vertices.append(Vertice(rotulo))
            self.num_vertices += 1
        else:
            print("Número máximo de vértices atingido.")

    def adicionar_arco(self, inicio, fim):
        self.matriz_adj[inicio][fim] = 1
		#grafos direcionados
		#self.matriz_adj[fim][inicio] = 1

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

    def warshall(self):
        n = self.num_vertices
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.matriz_adj[i][j] = self.matriz_adj[i][j] or (self.matriz_adj[i][k] and self.matriz_adj[k][j])
        print('transitivo finalizado')
        self.imprimir_matriz()

    '''        
    def original_marshal(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz_adj[i][j] == 1:
                    for k in range(self.num_vertices):
                        if self.matriz_adj[k][i] == 1:
                            self.matriz_adj[k][j] = 1
        print('transitivo finalizado')
        self.imprimir_matriz()
    '''

if __name__ == '__main__':
    main()
