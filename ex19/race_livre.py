# modulo thread deprecated

import os
import threading
import time
import random

x = 2

def main():
    os.system('clear')
    threads = []
    for i in range(5):
        t1 = threading.Thread(target=linhaA)
        t2 = threading.Thread(target=linhaB)
        t1.start()
        t2.start()
        threads.append(t1)
        threads.append(t2)
        time.sleep(3)
    for t in threads:
        t.join()

    print(f'O valor final de x é: {x}')

def linhaA():
    global x
    espera = random.randint(1, 3)
    time.sleep(espera)
    y = x
    y = y + 3
    x = y
    print(f'linhaA: novo valor de x = {x}')

def linhaB():
    global x
    espera = random.randint(1, 3)
    time.sleep(espera)
    y = x
    y = 2 * y
    x = y
    print(f'linhaB: novo valor de x = {x}')

if __name__ == '__main__':
    main()