# Encontre a posi¢do de um elemento em uma lista (Pesquisa Linear)

def main():
    vet = make_vet()
    target = int(input("alvo: "))
    
    posicao = search(vet, target)

    if posicao != -1:
        print(f"elemento {target} na posicao {posicao}.")
    else:
        print(f"elemento {target} nao esta na lista.")


def make_vet():
    length = int(input("digite o tamanho da lista: "))
    vector = []

    while length > 0:
        vector.append(int(input("item: ")))
        length -= 1

    return vector


def search(vet, target):
    for i in range(len(vet)):
        if vet[i] == target:
            return i
    return -1


main()




