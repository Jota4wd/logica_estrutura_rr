# Crie um vetor com valores intercalados de dois outros vetores

def main():
    vet1 = make_vet()
    vet2 = make_vet()
    vet_inter = []

    j = 0
    k = 0
    while j < len(vet1) or k < len(vet2):
        if j < len(vet1):
            vet_inter.append(vet1[j])
            j += 1

        if k < len(vet2):
            vet_inter.append(vet2[k])
            k += 1

    print(f'intercalado: {vet_inter}')


def make_vet():
    length = int(input("digite o tamanho da lista: "))
    vector = []

    while length > 0:
        vector.append(int(input("item: ")))
        length -= 1

    return vector


main()
