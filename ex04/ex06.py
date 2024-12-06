# Selecione os elementos pares de um vetor e copie para o segundo vetor.

def main():
    vet = make_vet()
    vet_even = []

    for i in vet:
        if i % 2 == 0:
            vet_even.append(i)

    print(f"vetor original: {vet}")
    print(f'vetor pares: {vet_even}')


def make_vet():
    length = int(input("digite o tamanho da lista: "))
    vector = []

    while length > 0:
        vector.append(int(input("item: ")))
        length -= 1

    return vector


main()
