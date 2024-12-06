import os
import random

os.system('clear')

def main():
    length = int(input('quantidade: '))
    a = []
    b = []
    i = 0
    j = 0

    while i < length:
        nbr = random.randint(1, length)
        if nbr not in a:
            a.append(nbr)
            i += 1

    while j < length:
        nbr = random.randint(1, length)
        if nbr not in b:
            b.append(nbr)
            j += 1

    a.sort()
    b.sort()
    c = intercalar_e_ordenar(a, b)
    print("lista c:", c)


def intercalar_e_ordenar(a, b):
    c = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


if __name__ == '__main__':
    main()
