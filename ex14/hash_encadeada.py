import os

def main():
    os.system('clear')
    tamanho = int(input('Tamanho da tabela: '))
    hash = TabelaHash(tamanho)
    while True:
        print('Escolha sua opção:')
        print('(M) -> Mostrar, (I) -> Inserir, (P) -> Procurar, (A) -> Apagar, (S) -> Sair')
        escolha = input('Opção: ').lower()
        if escolha == 'm':
            hash.mostra_tabela()
        elif escolha == 'i':
            valor = int(input('Valor a inserir: '))
            hash.inserir(ItemDado(valor))
        elif escolha == 'p':
            valor = int(input('Valor a encontrar: '))
            encontrado = hash.procurar(valor)
            if encontrado:
                print(f'Encontrado: {encontrado.obtem_dado()}')
            else:
                print('Não encontrado')
        elif escolha == 'a':
            valor = int(input('Valor a apagar: '))
            apagado = hash.apagar(valor)
            if apagado:
                print(f'Apagado: {apagado.obtem_dado()}')
            else:
                print('Não encontrado para apagar')
        elif escolha == 's':
            break
        else:
            print('Entrada inválida')


class ItemDado:
    def __init__(self, dado):
        self.dado = dado

    def obtem_dado(self):
        return self.dado


class Nodo:
    def __init__(self, item):
        self.item = item
        self.proximo = None


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz_hash = [[] for _ in range(tamanho)]

    def funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, item):
        chave = item.obtem_dado()
        valor_hash = self.funcao_hash(chave)
        novo_nodo = Nodo(item)
        self.matriz_hash[valor_hash].append(novo_nodo)

    def procurar(self, chave):
        valor_hash = self.funcao_hash(chave)
        for nodo in self.matriz_hash[valor_hash]:
            if nodo.item.obtem_dado() == chave:
                return nodo.item
        return None

    def apagar(self, chave):
        valor_hash = self.funcao_hash(chave)
        for nodo in self.matriz_hash[valor_hash]:
            if nodo.item.obtem_dado() == chave:
                self.matriz_hash[valor_hash].remove(nodo)
                return nodo.item
        return None

    def mostra_tabela(self):
        print('#########################')
        print('Tabela                  #')
        print('#########################')
        for i in range(self.tamanho):
            if self.matriz_hash[i]:
                print(f'Índice {i}: ', end='')
                for nodo in self.matriz_hash[i]:
                    print(nodo.item.obtem_dado(), end=' -> ')
                print('None')
            else:
                print(f'Índice {i}: *****')
        print('#########################')


if __name__ == '__main__':
    main()
