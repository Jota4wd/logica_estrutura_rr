# Receba um vetor elemento por elemento do teclado e coloque em uma lista.

def main():
    length = int(input("digite o tamanho da lista: "))
    list = []

    while length > 0:
        list.append(input("item: "))
        length -= 1

    print(list)


main()
