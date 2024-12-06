#quick in place

def main():
    length = int(input('quantidade: '))
    vet = []

    while length > 0:

        vet.append(int(input('valor: ')))
        length -= 1

    print(f'original:\n{vet}')
    quicksort_inplace(vet)
    print(f'ordenada:\n{vet}')

def quicksort_inplace(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start >= end:
        return

    # Particiona e obtém a posição final do pivô
    pivot_index = partition(array, start, end)

    # Recursivamente ordena as sublistas
    quicksort_inplace(array, start, pivot_index - 1)
    quicksort_inplace(array, pivot_index + 1, end)

def partition(array, start, end):
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


if __name__ == '__main__':
    main()
