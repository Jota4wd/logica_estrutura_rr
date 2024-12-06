#quicksort funcional

def main():
    length = int(input('quantidade: '))
    vet = []

    while length > 0:

        vet.append(int(input('valor: ')))
        length -= 1

    print(f'original:\n{vet}')
    vet_o = quicksort(vet)
    print(f'ordenada:\n{vet_o}')


def quick_sort(array):
    left = []
    right = []

    if len(array) <= 1:
        return array

    key = array[len(array) // 2]

    for i in array:
        if i < key:
            left.append(i)

        elif i > key:
            right.append(i)

    return quick_sort(left) + [key] + quick_sort(right)

if __name__ == '__main__':
    main()
