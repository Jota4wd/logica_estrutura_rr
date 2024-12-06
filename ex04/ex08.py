# Faca um programa para imprimir a tabuada de multiplicar

def main():
    multi = int(input('tabuada: '))

    i = 1
    while i <= 10:
        print(f'{multi} X {i} = {multi * i}')
        i += 1


if __name__ == "__main__":
    main()
