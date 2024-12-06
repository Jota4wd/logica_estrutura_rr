#bubble sort

def main():
    length = int(input('quantidade: '))
    vet = []

    while length > 0:

        vet.append(int(input('valor: ')))
        length -= 1

    print(f'original:\n{vet}')
    bubble_sort(vet)
    print(f'ordenada:\n{vet}')


def bubble_sort(vector):
    perms = True

    while perms:
        perms = False
        for i in range(len(vector) - 1):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i] #pythonico
                perms = True
    

if __name__ == '__main__':
    main()

