# Calcule a média aritmética dos elementos de um vetor

def main():
    vet = make_vet()


    sum = 0
    for i in vet:
        sum += i

    avg = sum / len(vet)
    print(f"a media eh: {avg}")


def make_vet():
    length = int(input("digite o tamanho da lista: "))
    vector = []

    while length > 0:
            vector.append(int(input("item: ")))
        length -= 1

    return vector


main()
