# selection sorte

def main():
    length = int(input('quantidade: '))
    vet = []

    while length > 0:

        vet.append(int(input('valor: ')))
        length -= 1

    print(f'original:\n{vet}')
    insertion_sort(vet)
    print(f'ordenada:\n{vet}')


def insertion_sort(vector):
    for i in range(1, len(vector)):
        for j in range(i, 0, -1):
            if vector[j] < vector[j - 1]:
                vector[j], vector[j - 1] = vector[j - 1], vector[j]
            else:
                break

