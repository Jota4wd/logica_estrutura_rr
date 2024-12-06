#faça um programa para imprimir as series abaixo
# b) 0,1,3,6,10,15.....n

def main():
    numero = int(input("n para as sequencias: "))

    sequencia_b(numero)


def sequencia_b(n):
    i = 0
    p = 1
    while i < n:
        print(i, end=", ")
        i = i + p
        p += 1
    print()


main()
