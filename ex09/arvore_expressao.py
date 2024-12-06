class Noh:
    def __init__(self, dado):
        # Inicializa um nó com um dado e ponteiros nulos
        self.esquerdo = None  # Filho esquerdo
        self.direito = None   # Filho direito
        self.dado = dado      # Valor armazenado (operador ou operando)
        
    def __str__(self):
        # Define como um nó será convertido para string
        return f"({self.dado})"
        
class ArvoreExpressao:
    def __init__(self):
        # Inicializa a árvore com raiz nula
        self.raiz = None
        
    def eh_operador(self, caractere):
        # Verifica se um caractere é um operador matemático
        return caractere in ['+', '-', '*', '/', '^']
        
    def criar_arvore_expressao(self, expressao):
        pilha = []  # Pilha para construir a árvore
        
        # Para cada caractere na expressão
        for char in expressao:
            if not self.eh_operador(char):
                # Se for um operando (número ou variável)
                pilha.append(Noh(char))  # Cria nó e empilha
            else:
                # Se for operador
                noh = Noh(char)  # Cria nó do operador
                # Liga aos dois últimos operandos (ordem importa!)
                noh.direito = pilha.pop()  # Último operando
                noh.esquerdo = pilha.pop()  # Penúltimo operando
                pilha.append(noh)  # Empilha a subárvore criada
                
        return pilha[0]  # Retorna a raiz da árvore
        
    def imprimir_em_ordem(self, raiz):
        # Imprime a expressão com parênteses usando percurso em ordem
        if raiz:
            if self.eh_operador(raiz.dado):
                print("(", end="")
            self.imprimir_em_ordem(raiz.esquerdo)  # Visita esquerda
            print(raiz.dado, end="")               # Visita raiz
            self.imprimir_em_ordem(raiz.direito)   # Visita direita
            if self.eh_operador(raiz.dado):
                print(")", end="")