import os

def main():
    os.system('clear')
    tamanho = int(input('tamanho da tabela: '))
    quantidade = int(input('quantidade inicial de itens: '))
    hash = TabelaHash(tamanho)
    while True:
        print('escolha escolha sua opcao:')
        print('(M) -> mostrar, (I) -> inserir, (P) -> procurar, (S) -> sair')
        escolha = input('opcao: ').lower()
        if escolha == 'm':
            hash.mostra_tabela()
        elif escolha == 'i':
            valor = int(input('valor a inserir: '))
            hash.inserir(ItemDado(valor))
        elif escolha == 'p':
            valor = int(input('valor a encontrar: '))
            encontrar = hash.procurar(valor)
            if encontrar != -1:
                print('encontrado: {valor}')
            else:
                print('nao encontrado')
        elif escolha == 's':
            break
        else:
            print('entrada invalida')


class ItemDado:
    def __init__(self, dado):
        self.dado = dado

    def obtem_dado(self):
        return self.dado


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz_hash = []
        for i in range(tamanho):
            self.matriz_hash.append(None)

    def mostra_tabela(self):
        print('#########################')
        print('tabela                  #')
        print('#########################')
        for i in range(self.tamanho):
            if self.matriz_hash[i] != None:
                print(self.matriz_hash[i].obtem_dado())
            else:
                print('*****')
        print('#########################')

    def funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, item):
        chave = item.obtem_dado()
        valor_hash = self.funcao_hash(chave)
        while self.matriz_hash[valor_hash] != None and self.matriz_hash[valor_hash] != 'DELETED':
            valor_hash += 1
            valor_hash %= self.tamanho
        self.matriz_hash[valor_hash] = item

    def apagar(self, chave):
        valor_hash = self.funcao_hash(chave)
        while self.matriz_hash[valor_hash] != None:
            if self.matriz_hash[valor_hash].obter_chave == chave:
                temp = self.matriz_hash[valor_hash]
                self.matriz.hash[valor_hash] = 'DELETED'
                return temp
            valor_hash += 1
            valor_hash %= self.tamanho
        return None

    def encontrar(self, chave):
        valor_hash = self.funcao_hash(chave)
        while self.matriz_hash[valor_hash] != None:
            if self.matriz_hash[valor_hash].obter_chave == chave:
                return self.matriz_hash[valor_hash]
            valor_hash += 1
            valor_hash %= self.tamanho
        return None


if __name__ == '__main__':
    main()
