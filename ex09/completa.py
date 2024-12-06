from collections import deque
import random

class Noh:
    def __init__(self, dado=0, esquerdo=None, direito=None, altura=1):
        self.dado = dado
        self.esquerdo = esquerdo
        self.direito = direito
        self.altura = altura  # Para balanceamento AVL

    def __str__(self):
        return f'{self.dado}'


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def criaNoh(self, dado):
        return Noh(dado)

    def getAltura(self, raiz):
        if raiz is None:
            return 0
        return raiz.altura

    def getFatorBalanceamento(self, raiz):
        if raiz is None:
            return 0
        return self.getAltura(raiz.esquerdo) - self.getAltura(raiz.direito)

    def atualizaAltura(self, raiz):
        if raiz is None:
            return
        raiz.altura = max(self.getAltura(raiz.esquerdo), 
                         self.getAltura(raiz.direito)) + 1

    def rotacaoDireita(self, y):
        x = y.esquerdo
        T2 = x.direito

        x.direito = y
        y.esquerdo = T2

        y.altura = max(self.getAltura(y.esquerdo), 
                      self.getAltura(y.direito)) + 1
        x.altura = max(self.getAltura(x.esquerdo), 
                      self.getAltura(x.direito)) + 1

        return x

    def rotacaoEsquerda(self, x):
        y = x.direito
        T2 = y.esquerdo

        y.esquerdo = x
        x.direito = T2

        x.altura = max(self.getAltura(x.esquerdo), 
                      self.getAltura(x.direito)) + 1
        y.altura = max(self.getAltura(y.esquerdo), 
                      self.getAltura(y.direito)) + 1

        return y

    def insere(self, raiz, dado):
        if raiz is None:
            return self.criaNoh(dado)

        if dado < raiz.dado:
            raiz.esquerdo = self.insere(raiz.esquerdo, dado)
        elif dado > raiz.dado:
            raiz.direito = self.insere(raiz.direito, dado)
        else:
            return raiz  # Dados iguais não são permitidos

        raiz.altura = max(self.getAltura(raiz.esquerdo),
                         self.getAltura(raiz.direito)) + 1

        balanceamento = self.getFatorBalanceamento(raiz)

        # Casos de balanceamento
        # Caso Esquerda-Esquerda
        if balanceamento > 1 and dado < raiz.esquerdo.dado:
            return self.rotacaoDireita(raiz)

        # Caso Direita-Direita
        if balanceamento < -1 and dado > raiz.direito.dado:
            return self.rotacaoEsquerda(raiz)

        # Caso Esquerda-Direita
        if balanceamento > 1 and dado > raiz.esquerdo.dado:
            raiz.esquerdo = self.rotacaoEsquerda(raiz.esquerdo)
            return self.rotacaoDireita(raiz)

        # Caso Direita-Esquerda
        if balanceamento < -1 and dado < raiz.direito.dado:
            raiz.direito = self.rotacaoDireita(raiz.direito)
            return self.rotacaoEsquerda(raiz)

        return raiz

    def inserir_aleatorio(self, quantidade, min_valor=1, max_valor=100):
        """Insere quantidade especificada de valores aleatórios na árvore"""
        for _ in range(quantidade):
            valor = random.randint(min_valor, max_valor)
            self.raiz = self.insere(self.raiz, valor)

    def apaga(self, raiz, dado):
        if raiz is None:
            return raiz

        if dado < raiz.dado:
            raiz.esquerdo = self.apaga(raiz.esquerdo, dado)
        elif dado > raiz.dado:
            raiz.direito = self.apaga(raiz.direito, dado)
        else:
            if raiz.esquerdo is None:
                return raiz.direito
            elif raiz.direito is None:
                return raiz.esquerdo
            else:
                temp = self.menorValor(raiz.direito)
                raiz.dado = temp.dado
                raiz.direito = self.apaga(raiz.direito, temp.dado)

        if raiz is None:
            return raiz

        # Atualiza altura e balanceia após remoção
        raiz.altura = max(self.getAltura(raiz.esquerdo),
                         self.getAltura(raiz.direito)) + 1

        balanceamento = self.getFatorBalanceamento(raiz)

        # Casos de balanceamento após remoção
        # Caso Esquerda-Esquerda
        if balanceamento > 1 and self.getFatorBalanceamento(raiz.esquerdo) >= 0:
            return self.rotacaoDireita(raiz)

        # Caso Esquerda-Direita
        if balanceamento > 1 and self.getFatorBalanceamento(raiz.esquerdo) < 0:
            raiz.esquerdo = self.rotacaoEsquerda(raiz.esquerdo)
            return self.rotacaoDireita(raiz)

        # Caso Direita-Direita
        if balanceamento < -1 and self.getFatorBalanceamento(raiz.direito) <= 0:
            return self.rotacaoEsquerda(raiz)

        # Caso Direita-Esquerda
        if balanceamento < -1 and self.getFatorBalanceamento(raiz.direito) > 0:
            raiz.direito = self.rotacaoDireita(raiz.direito)
            return self.rotacaoEsquerda(raiz)

        return raiz

    def pesquisa(self, raiz, valor):
        """Retorna o nó se encontrado, None caso contrário"""
        if raiz is None or raiz.dado == valor:
            return raiz
        
        if valor < raiz.dado:
            return self.pesquisa(raiz.esquerdo, valor)
        return self.pesquisa(raiz.direito, valor)

    def menorValor(self, raiz):
        if raiz is None:
            return None
        if raiz.esquerdo is None:
            return raiz
        return self.menorValor(raiz.esquerdo)

    def maiorValor(self, raiz):
        if raiz is None:
            return None
        if raiz.direito is None:
            return raiz
        return self.maiorValor(raiz.direito)

    def profundidadeMaxima(self, raiz):
        if raiz is None:
            return 0
        profundidade_esquerda = self.profundidadeMaxima(raiz.esquerdo)
        profundidade_direita = self.profundidadeMaxima(raiz.direito)
        return max(profundidade_esquerda, profundidade_direita) + 1
    
    def tamanho(self, raiz):
        if raiz is None:
            return 0
        return self.tamanho(raiz.esquerdo) + self.tamanho(raiz.direito) + 1

    def ehBST(self, raiz, min_valor=float('-inf'), max_valor=float('inf')):
        """Verifica se a árvore é uma BST válida"""
        if raiz is None:
            return True

        if raiz.dado <= min_valor or raiz.dado >= max_valor:
            return False

        return (self.ehBST(raiz.esquerdo, min_valor, raiz.dado) and
                self.ehBST(raiz.direito, raiz.dado, max_valor))
    
    # Diferentes tipos de travessia
    def travessiaPreOrdem(self, raiz):
        """Raiz -> Esquerda -> Direita"""
        if raiz is None:
            return
        print(f'{raiz.dado}', end=' ')
        self.travessiaPreOrdem(raiz.esquerdo)
        self.travessiaPreOrdem(raiz.direito)

    def travessiaEmOrdem(self, raiz):
        """Esquerda -> Raiz -> Direita"""
        if raiz is None:
            return
        self.travessiaEmOrdem(raiz.esquerdo)
        print(f'{raiz.dado}', end=' ')
        self.travessiaEmOrdem(raiz.direito)

    def travessiaPosOrdem(self, raiz):
        """Esquerda -> Direita -> Raiz"""
        if raiz is None:
            return
        self.travessiaPosOrdem(raiz.esquerdo)
        self.travessiaPosOrdem(raiz.direito)
        print(f'{raiz.dado}', end=' ')

    def travessiaPorNivel(self, raiz):
        """Travessia em largura (breadth-first)"""
        if raiz is None:
            return

        fila = deque([raiz])
        while fila:
            nivel_atual = len(fila)
            for _ in range(nivel_atual):
                noh = fila.popleft()
                print(f'{noh.dado}', end=' ')

                if noh.esquerdo:
                    fila.append(noh.esquerdo)
                if noh.direito:
                    fila.append(noh.direito)
            print()  # Nova linha para cada nível

    def imprimirArvore(self, raiz):
        if raiz is None:
            return
        self.imprimirArvore(raiz.esquerdo)
        print(f'{raiz.dado}')
        self.imprimirArvore(raiz.direito)

    def imprimeArvoreInvertida(self, raiz):
        if raiz is None:
            return
        self.imprimeArvoreInvertida(raiz.direito)
        print(f'{raiz.dado}')
        self.imprimeArvoreInvertida(raiz.esquerdo)

    def imprimeNohs(self, raiz):
        """Versão melhorada e mais segura"""
        if raiz is None:
            return
            
        dado = raiz.dado
        esq = "None" if raiz.esquerdo is None else raiz.esquerdo.dado
        dir = "None" if raiz.direito is None else raiz.direito.dado
        
        print(f'{{{dado}[{esq},{dir}]}}')
        self.imprimeNohs(raiz.esquerdo)
        self.imprimeNohs(raiz.direito)

    def imprimirArvoreVisual(self, raiz, nivel=0, prefixo="Raiz: "):
        """Imprime a árvore de forma visual"""
        if raiz is None:
            return
        
        espacos = "    " * nivel
        print(f"{espacos}{prefixo}{raiz.dado}")
        
        if raiz.esquerdo:
            self.imprimirArvoreVisual(raiz.esquerdo, nivel + 1, "E-- ")
        if raiz.direito:
            self.imprimirArvoreVisual(raiz.direito, nivel + 1, "D-- ")