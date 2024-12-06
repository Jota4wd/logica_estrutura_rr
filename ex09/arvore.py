import random

class Noh:
    def __init__(self, dado=0, esquerdo=None, direito=None):
        self.dado = dado
        self.esquerdo = esquerdo
        self.direito = direito

    def __str__(self):
        return f'{self.dado}'


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def criaNoh(self, dado):
        return Noh(dado)

    def insere(self, raiz, dado):
        if raiz is None:
            return self.criaNoh(dado)
        if dado < raiz.dado:
            raiz.esquerdo = self.insere(raiz.esquerdo, dado)
        else:
            raiz.direito = self.insere(raiz.direito, dado)
        return raiz

    def inserir_aleatorio(self, quantidade, min_valor=1, max_valor=100):
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
        return raiz

    def pesquisa(self, raiz, valor):
        if raiz is None:
            return False
        if valor == raiz.dado:
            return True
        elif valor < raiz.dado:
            return self.pesquisa(raiz.esquerdo, valor)
        else:
            return self.pesquisa(raiz.direito, valor)

    def menorValor(self, raiz):
        if raiz is None:
            return None
        if raiz.esquerdo is None:
            return raiz
        return self.menorValor(raiz.esquerdo)

    def profundidadeMaxima(self, raiz):
        if raiz is None:
            return 0
        profundidade_esquerda = self.profundidadeMaxima(raiz.esquerdo)
        profundidade_direita = self.profundidadeMaxima(raiz.direito)
        return max(profundidade_esquerda, profundidade_direita) + 1
    
    def tamanho(self, raiz):
        if raiz is None:
            return 0
        tamanho_esquerda = self.tamanho(raiz.esquerdo)
        tamanho_direita = self.tamanho(raiz.direito)
        return tamanho_esquerda + tamanho_direita + 1
    
    def imprimirArvore(self, raiz):
        if raiz is None:
            return
        self.imprimirArvore(raiz.esquerdo)
        print(f'{raiz.dado}')  # Corrigido para usar a variável raiz
        self.imprimirArvore(raiz.direito)

    def imprimeArvoreInvertida(self, raiz):
        if raiz is None:
            return
        self.imprimeArvoreInvertida(raiz.direito)
        print(f'{raiz.dado}')  # Corrigido para usar a variável raiz
        self.imprimeArvoreInvertida(raiz.esquerdo)

    def imprimeNohs(self, raiz):
        if raiz is None:
            return
        a = raiz.dado
        b = None
        c = None
        
        if raiz.esquerdo is not None:
            b = raiz.esquerdo.dado
        if raiz.direito is not None:
            c = raiz.direito.dado
            
        print(f'{{{a}[{b},{c}]}}')
        self.imprimeNohs(raiz.esquerdo)
        self.imprimeNohs(raiz.direito)