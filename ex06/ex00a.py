#desafio proposto para a propria funcao append e pop

def main():
    elementos = []

    jj_append(elementos, 1)
    jj_append(elementos, 2)
    jj_append(elementos, 3)
    jj_append(elementos, 4)

    print("Lista após append:", elementos)

    ultimo = jj_pop(elementos)

    print("Elemento removido:", ultimo)
    print("Lista após pop:", elementos)

    outro = jj_pop(elementos, 1)

    print("Elemento removido por indice:", outro)
    print("Lista após pop:", elementos)


def jj_append(elementos, elemento):
    elementos += [elemento]

def jj_pop(elementos, indice=None):
    if not elementos:  # Comportamento padrão da função pop
        raise IndexError("pop from empty list")

    if indice is not None:
        if indice < 0 or indice >= len(elementos):
            raise IndexError("pop index out of range")

        elemento_removido = elementos[indice]
        elementos[:] = elementos[:indice] + elementos[indice + 1:]
        return elemento_removido

    ultimo_elemento = elementos[-1]
    elementos[:] = elementos[:-1]
    return ultimo_elemento


if __name__ == "__main__":
    main()
