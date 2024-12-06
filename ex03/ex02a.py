#faça um programa para imprimir as series abaixo
# a) 2,4,16,256........n

def main():
    numero = int(input("valor maximo para a sequencia: "))

    sequencia_a(numero)


def sequencia_a(n):
    i = 2
    while i < n:
        print(i, end=", ")
        i = i ** 2
    print()


main()
