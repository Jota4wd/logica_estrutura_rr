from heapq import heappush, heappop, heapify  # Para fila de prioridade

class NohHuffman:
    def __init__(self, char, freq):
        # Inicializa nó para árvore de Huffman
        self.char = char      # Caractere
        self.freq = freq      # Frequência do caractere
        self.esquerdo = None  # Filho esquerdo
        self.direito = None   # Filho direito
        
    def __lt__(self, outro):
        # Define como comparar dois nós (pela frequência)
        return self.freq < outro.freq

class Huffman:
    def __init__(self):
        self.raiz = None     # Raiz da árvore
        self.codigos = {}    # Dicionário de códigos binários
        
    def calcular_frequencia(self, texto):
        # Conta frequência de cada caractere no texto
        frequencias = {}
        for char in texto:
            frequencias[char] = frequencias.get(char, 0) + 1
        return frequencias
        
    def criar_arvore(self, texto):
        # Calcula frequência dos caracteres
        frequencias = self.calcular_frequencia(texto)
        
        # Cria fila de prioridade com nós iniciais
        heap = []
        for char, freq in frequencias.items():
            heappush(heap, NohHuffman(char, freq))
            
        # Constrói a árvore juntando nós de menor frequência
        while len(heap) > 1:
            esq = heappop(heap)  # Remove menor frequência
            dir = heappop(heap)  # Remove segundo menor
            
            # Cria nó interno com soma das frequências
            interno = NohHuffman(None, esq.freq + dir.freq)
            interno.esquerdo = esq
            interno.direito = dir
            
            heappush(heap, interno)  # Adiciona nó interno à fila
            
        self.raiz = heap[0]  # Último nó é a raiz
        
    def gerar_codigos(self, raiz=None, codigo=""):
        # Gera código binário para cada caractere (recursivamente)
        if raiz is None:
            raiz = self.raiz
            
        if raiz.char is not None:  # Se é folha (tem caractere)
            self.codigos[raiz.char] = codigo
            return
            
        # Percorre esquerda (adiciona 0) e direita (adiciona 1)
        self.gerar_codigos(raiz.esquerdo, codigo + "0")
        self.gerar_codigos(raiz.direito, codigo + "1")