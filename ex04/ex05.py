# Selecione os elementos pares de um vetor

def main():
    vet = make_vet()

    for i in vet:
        if i % 2 == 0:
            print(i, end=", ")

    print()


def make_vet():
    length = int(input("digite o tamanho da lista: "))
    vector = []

    while length > 0:
        vector.append(int(input("item: ")))
        length -= 1

    return vector


main()
