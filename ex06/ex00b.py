#desafio proposto para a propria funcao append e pop
#codigo proposto por ias usando classe, apos pedir correcao para meu codigo


def main():
    minha_lista = MinhaLista()
    minha_lista.append(1)
    minha_lista.append(2)
    minha_lista.append(3)

    print("Lista após append:", minha_lista)

    ultimo = minha_lista.pop()
    print("Elemento removido:", ultimo)
    print("Lista após pop:", minha_lista)


class MinhaLista:
    def __init__(self):
        self.elementos = []  # Inicializa uma lista vazia para armazenar os elementos

    def append(self, elemento):
        # Adiciona um elemento ao final da lista
        self.elementos += [elemento]  # Usando concatenação para simular o append

    def pop(self):
        # Remove e retorna o último elemento da lista
        if not self.elementos:  # Verifica se a lista está vazia
            raise IndexError("pop from empty list")  # Lança um erro se a lista estiver vazia
        ultimo_elemento = self.elementos[-1]  # Obtém o último elemento
        self.elementos = self.elementos[:-1]  # Remove o último elemento
        return ultimo_elemento  # Retorna o elemento removido

    def __str__(self):
        return str(self.elementos)  # Método para imprimir a lista de forma legível


if __name__ == "__main__":
    main()
