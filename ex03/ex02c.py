#faça um programa para imprimir as series abaixo
# c) 0,N,1,N-1,2,n-2...n,0

def main():
    numero = int(input("n para as sequencias: "))

    sequencia_c(numero)


def sequencia_c(n):
    i = 0
    while i < (n + 1):
        print(i, end=", ")
        print(n - i, end=", ")
        i += 1
    print()


main()
