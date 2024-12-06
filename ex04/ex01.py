# selecione o maior e o menor elemento de um vetor

def main():
    length = 5

    list = []

    while length > 0:
        list.append(int(input("item: ")))
        length -= 1

    bigger = list[0]
    smaller = list[0]

    for i in list:
        if i > bigger:
            bigger = i
        if i < smaller:
            smaller = i

    print(f"o maior item eh: {bigger}")
    print(f"o menor item eh: {smaller}")


main()
