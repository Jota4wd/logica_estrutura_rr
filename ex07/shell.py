#shell sorte, alguns chamam de colunas outros de espaços, mas pelo q eu entendi sao apenas sub listas

def main():
    length = int(input('quantidade: '))
    vet = []

    while length > 0:

        vet.append(int(input('valor: ')))
        length -= 1

    print(f'original:\n{vet}')
    shell_sort(vet)
    print(f'ordenada:\n{vet}')


def shell_sort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp

        gap //= 2

    return array


if __name__ == '__main__':
    main()
