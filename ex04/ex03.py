# Receba um vetor e inverta a ordem dos elementos (Sem usar a funcdo reverse)

def main():
    vet = make_vet()

    print(f"sequencia digitada: {vet}")

    inicio = 0
    fim = len(vet) - 1

    while inicio < fim :
        temp = vet[inicio]
        vet[inicio] = vet[fim]
        vet[fim] = temp
        inicio += 1
        fim -= 1

    print(f"sequencia invertida: {vet}")


def make_vet():
    length = int(input("digite o tamanho da lista: "))
    vector = []

    while length > 0:
        vector.append(int(input("item: ")))
        length -= 1

    return vector


main()
