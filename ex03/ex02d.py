#faça um programa para imprimir as series abaixo
# d) 1,1,2,3,5,8.......n

def main():
    numero = int(input("n para as sequencias: "))

    sequencia_d(numero)
    print("pythonica")
    sequencia_pythonica(numero)


def sequencia_d(n):
    a, b = 0, 1
    while n > 0:
        print(b, end=", ")
        temp = a
        a = b
        b = temp + a
        n -= 1
    print()


def sequencia_pythonica(n):
    a, b = 0, 1
    while n > 0:
        print(b, end=", ")
        a, b = b, a + b
        n -= 1
    print()

main()
