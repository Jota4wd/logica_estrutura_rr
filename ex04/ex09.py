# Simule um odometro digital no video com (por exemplo) segundos, minutos e horas

import os

def main():
    os.system('clear')
    i = 1
    while i < 23:
        j = 0
        while j < 60:
            k = 0
            while k < 60:
                os.system('clear')
                print(f'{i:02d}:{j:02d}:{k:02d}')
                k += 1

            j += 1

        i += 1


if __name__ == '__main__':
    main()
