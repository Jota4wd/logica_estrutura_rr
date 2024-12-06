# tambem ja conhecia o bubble em c, e tentei converter para python

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
    for i in range(len(vector)):
        trocou = False

        for j in range(len(vector) - 1, i, -1):
            if vector[j] < vector[j - 1]:
                vector[j], vector[j - 1] = vector[j - 1], vector[j]
                trocou = True

        if not trocou:
            break

