# Faca um programa para imprimir a tabuada de multiplicar

def main():
    i = 1
    while i <= 10:
        j = 1
        print()
        while j <= 10:
            print(f'{i} X {j:2d} = {j * i:3d}')
            j += 1

        i += 1


if __name__ == "__main__":
    main()
