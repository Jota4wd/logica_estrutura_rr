# aprendi com david buzatto q dos ordenadores bosta o menos bosta eh o insertion sort
# como vamos começar um modulo com alguns desses, vou deixar a implementaçao dele em python

import os
from datetime import datetime
os.system('clear')

def main():
    length = int(input('quantidade: '))
    vet = []

    while length > 0:

        vet.append(int(input('valor: ')))
        length -= 1

    print(f'original:\n{vet}')
    insertion_sort(vet)
    print(f'ordenada:\n{vet}')

def insertion_sort(vetor):
    i = 1

    while i < len(vetor):
        j = i

        while j > 0:
            if vetor[j] < vetor[j - 1]:
                tmp = vetor[j - 1]
                vetor[j - 1] = vetor[j]
                vetor[j] = tmp

            else:
                break

            j -= 1

        i += 1


if __name__ == '__main__':
    main()
