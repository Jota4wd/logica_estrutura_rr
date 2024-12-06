import os

def main():
    os.system('clear')
    tamanho = int(input('tamanho da tabela: '))
    hash = TabelaHash(tamanho)
    while True:
        print('escolha escolha sua opcao:')
        print('(M) -> mostrar, (I) -> inserir, (P) -> procurar, (R) -> remover, (S) -> sair')
        escolha = input('opcao: ').lower()
        if escolha == 'm':
            hash.mostra_tabela()
        elif escolha == 'i':
            valor = int(input('valor a inserir: '))
            if hash.inserir(ItemDado(valor)):
                print('Valor inserido com sucesso')
            else:
                print('Tabela cheia - não foi possível inserir')
        elif escolha == 'p':
            valor = int(input('valor a procurar: '))
            procurar = hash.procurar(valor)
            if procurar is not None:
                print(f'encontrado: {valor}')
            else:
                print('nao encontrado')
        elif escolha == 'r':
            valor = int(input('valor a remover: '))
            if hash.apagar(valor):
                print('Valor removido com sucesso')
            else:
                print('Valor não encontrado')
        elif escolha == 's':
            break
        else:
            print('entrada invalida')


class ItemDado:
    def __init__(self, dado):
        self.dado = dado
        self.deletado = False

    def obtem_dado(self):
        return self.dado

    def esta_deletado(self):
        return self.deletado

    def marcar_deletado(self):
        self.deletado = True


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz_hash = [None] * tamanho
        self.quantidade_itens = 0

    def mostra_tabela(self):
        print('#########################')
        print('tabela                  #')
        print('#########################')
        for i in range(self.tamanho):
            if self.matriz_hash[i] is not None:
                if self.matriz_hash[i].esta_deletado():
                    print('(deletado)')
                else:
                    print(self.matriz_hash[i].obtem_dado())
            else:
                print('*****')
        print('#########################')

    def funcao_hash1(self, chave):
        return chave % self.tamanho

    def funcao_hash2(self, chave):
        # Garantindo que o deslocamento nunca será 0 e será menor que o tamanho da tabela
        return 1 + (chave % (self.tamanho - 1))

    def esta_cheia(self):
        return self.quantidade_itens >= self.tamanho

    def inserir(self, item):
        if self.esta_cheia():
            return False

        valor_hash = self.funcao_hash1(item.obtem_dado())
        deslocamento = self.funcao_hash2(item.obtem_dado())
        
        primeira_pos_deletada = -1
        tentativas = 0
        
        while tentativas < self.tamanho:
            if self.matriz_hash[valor_hash] is None:
                if primeira_pos_deletada != -1:
                    self.matriz_hash[primeira_pos_deletada] = item
                else:
                    self.matriz_hash[valor_hash] = item
                self.quantidade_itens += 1
                return True
            elif self.matriz_hash[valor_hash].esta_deletado() and primeira_pos_deletada == -1:
                primeira_pos_deletada = valor_hash
            
            valor_hash = (valor_hash + deslocamento) % self.tamanho
            tentativas += 1
        
        if primeira_pos_deletada != -1:
            self.matriz_hash[primeira_pos_deletada] = item
            self.quantidade_itens += 1
            return True
            
        return False

    def apagar(self, chave):
        valor_hash = self.funcao_hash1(chave)
        deslocamento = self.funcao_hash2(chave)
        
        tentativas = 0
        while self.matriz_hash[valor_hash] is not None and tentativas < self.tamanho:
            if not self.matriz_hash[valor_hash].esta_deletado() and self.matriz_hash[valor_hash].obtem_dado() == chave:
                self.matriz_hash[valor_hash].marcar_deletado()
                self.quantidade_itens -= 1
                return True
            valor_hash = (valor_hash + deslocamento) % self.tamanho
            tentativas += 1
        return False

    def procurar(self, chave):
        valor_hash = self.funcao_hash1(chave)
        deslocamento = self.funcao_hash2(chave)
        
        tentativas = 0
        while self.matriz_hash[valor_hash] is not None and tentativas < self.tamanho:
            if not self.matriz_hash[valor_hash].esta_deletado() and self.matriz_hash[valor_hash].obtem_dado() == chave:
                return self.matriz_hash[valor_hash]
            valor_hash = (valor_hash + deslocamento) % self.tamanho
            tentativas += 1
        return None


if __name__ == '__main__':
    main()
