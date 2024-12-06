import os

def main():
    os.system('clear')
    arvore = Arvore234()
    arvore.inserir(50)
    arvore.inserir(40)
    arvore.inserir(60)
    arvore.inserir(30)
    arvore.inserir(70)

    while True:
        print('\nEscolha sua opcao')
        print('M -> mostrar, I -> inserir, P -> procurar, S -> sair')
        print('O -> em ordem, N -> menor, X -> maior')
        escolha = input('opcao: ').lower()

        if escolha == 'm':
            arvore.mostrar_arvore()
        elif escolha == 'i':
            valor = int(input('valor: '))
            arvore.inserir(valor)
        elif escolha == 'p':
            valor = int(input('valor: '))
            encontrar = arvore.procurar(valor)
            if encontrar != -1:
                print(f'encontrado: {valor}')
            else:
                print('nao encontrado')
        elif escolha == 'o':
            arvore.imprimir_em_ordem()
        elif escolha == 'n':
            menor = arvore.encontrar_menor()
            print(f'Menor elemento: {menor}')
        elif escolha == 'x':
            maior = arvore.encontrar_maior()
            print(f'Maior elemento: {maior}')
        elif escolha == 's':
            break
        else:
            print('entrada invalida')


class ItemDado:
    def __init__(self, dado):
        self.dado = dado

    def __str__(self):
        return f'/{self.dado}'

    def mostrar_item(self):
        print(f'/{self.dado}')

class Noh:
    def __init__(self):
        self.ORDEM = 4
        self.numero_itens = 0
        self.pai = None
        self.lista_dados = [None] * 3  # Mudança aqui
        self.lista_filhos = [None] * 4

    def conectar_filho(self, numero_filho, filho):
        self.lista_filhos[numero_filho] = filho
        if filho is not None:
            filho.pai = self

    def desconectar_filho(self, numero_filho):
        noh_temp = self.lista_filhos[numero_filho]
        self.lista_filhos[numero_filho] = None
        return noh_temp

    def obtem_filho(self, numero_filho):
        return self.lista_filhos[numero_filho]

    def obtem_pai(self):
        return self.pai

    def eh_folha(self):
        return self.lista_filhos[0] is None

    def obtem_numero_itens(self):
        return self.numero_itens

    def obtem_item(self, indice):
        return self.lista_dados[indice]

    def esta_cheio(self):
        return self.numero_itens == self.ORDEM - 1

    def procurar_item(self, chave):
        for i in range(self.numero_itens):
            if self.lista_dados[i].dado == chave:
                return i
        return -1

    def inserir_item(self, novo_item):
        # Guarda o novo item
        nova_chave = novo_item.dado

        # Se não há items, insere na primeira posição
        if self.numero_itens == 0:
            self.lista_dados[0] = novo_item
            self.numero_itens += 1
            return 0

        # Começa do último item e move items maiores uma posição para direita
        i = self.numero_itens - 1
        while i >= 0:
            if self.lista_dados[i].dado > nova_chave:
                self.lista_dados[i + 1] = self.lista_dados[i]
                i -= 1
            else:
                break

        # Insere o novo item
        self.lista_dados[i + 1] = novo_item
        self.numero_itens += 1
        return i + 1

    def remove_item(self):
        temp = self.lista_dados[self.numero_itens - 1]
        self.lista_dados[self.numero_itens - 1] = None
        self.numero_itens -= 1
        return temp

    def mostrar_noh(self):
        valores = ''
        for i in range(self.numero_itens):
            valores += f'/{self.lista_dados[i].dado}'
        return valores


class Arvore234:
    def __init__(self):
        self.raiz = Noh()

    def procurar(self, chave):
        noh_atual = self.raiz
        while True:
            numero_filho = noh_atual.procurar_item(chave)
            if numero_filho != -1:
                return numero_filho
            elif noh_atual.eh_folha():
                return -1
            else:
                noh_atual = self.obtem_proximo_filho(noh_atual, chave)

    def inserir(self, valor):
        noh_atual = self.raiz
        temp_item = ItemDado(valor)
        while True:
            if noh_atual.esta_cheio():
                self.separar(noh_atual)
                noh_atual = noh_atual.obtem_pai()
                noh_atual = self.obtem_proximo_filho(noh_atual, valor)
            elif noh_atual.eh_folha():
                break
            else:
                noh_atual = self.obtem_proximo_filho(noh_atual, valor)
        noh_atual.inserir_item(temp_item)

    def separar(self, noh):
        item_c = noh.remove_item()
        item_b = noh.remove_item()
        filho2 = noh.desconectar_filho(2)
        filho3 = noh.desconectar_filho(3)
        novo_direito = Noh()

        if noh == self.raiz:
            self.raiz = Noh()
            pai = self.raiz
            self.raiz.conectar_filho(0, noh)
        else:
            pai = noh.obtem_pai()

        indice_item = pai.inserir_item(item_b)
        n = pai.obtem_numero_itens()

        for j in range(n-1, indice_item, -1):
            temp = pai.desconectar_filho(j)
            pai.conectar_filho(j+1, temp)

        pai.conectar_filho(indice_item + 1, novo_direito)
        novo_direito.inserir_item(item_c)
        novo_direito.conectar_filho(0, filho2)
        novo_direito.conectar_filho(1, filho3)

    def obtem_proximo_filho(self, noh, valor):
        for i in range(noh.obtem_numero_itens()):
            if valor < noh.obtem_item(i).dado:
                return noh.obtem_filho(i)
        return noh.obtem_filho(noh.obtem_numero_itens())

    def mostrar_arvore(self):
        self.r_mostrar_arvore(self.raiz, 0, 0)

    def r_mostrar_arvore(self, noh, nivel, numero_filho):
        if noh is not None:
            print(f'Nivel = {nivel} Filho = {numero_filho}', end='')
            print(noh.mostrar_noh())
            for j in range(noh.obtem_numero_itens() + 1):
                proximo_noh = noh.obtem_filho(j)
                if proximo_noh is not None:
                    self.r_mostrar_arvore(proximo_noh, nivel + 1, j)

    def encontrar_menor(self):
        if self.raiz is None:
            return None

        noh_atual = self.raiz
        # Vai sempre para o filho mais à esquerda até chegar em uma folha
        while not noh_atual.eh_folha():
            noh_atual = noh_atual.obtem_filho(0)

        # Retorna o primeiro item do nó folha mais à esquerda
        return noh_atual.obtem_item(0).dado

    def encontrar_maior(self):
        if self.raiz is None:
            return None

        noh_atual = self.raiz
        # Vai sempre para o filho mais à direita até chegar em uma folha
        while not noh_atual.eh_folha():
            noh_atual = noh_atual.obtem_filho(noh_atual.obtem_numero_itens())

        # Retorna o último item do nó folha mais à direita
        return noh_atual.obtem_item(noh_atual.obtem_numero_itens() - 1).dado

    def imprimir_em_ordem(self):
        print("Árvore em ordem:", end=" ")
        self._imprimir_em_ordem(self.raiz)
        print()

    def _imprimir_em_ordem(self, noh):
        if noh is not None:
            # Processa primeiro filho
            self._imprimir_em_ordem(noh.obtem_filho(0))

            # Processa primeiro item e segundo filho
            if noh.obtem_numero_itens() > 0:
                print(noh.obtem_item(0).dado, end=" ")
                self._imprimir_em_ordem(noh.obtem_filho(1))

            # Processa segundo item e terceiro filho
            if noh.obtem_numero_itens() > 1:
                print(noh.obtem_item(1).dado, end=" ")
                self._imprimir_em_ordem(noh.obtem_filho(2))

            # Processa terceiro item e quarto filho
            if noh.obtem_numero_itens() > 2:
                print(noh.obtem_item(2).dado, end=" ")
                self._imprimir_em_ordem(noh.obtem_filho(3))

if __name__ == '__main__':
    main()
