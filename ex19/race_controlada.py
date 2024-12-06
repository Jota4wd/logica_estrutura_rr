# modulo thread deprecated
  
import os
import threading
import time
import random

x = 2
tlock = threading.Lock()

def main():
    os.system('clear')
    for i in range(20):
        threading.Thread(target=linhaA).start()
        threading.Thread(target=linhaB).start()
        time.sleep(3)
        print(f'O valor final de x é: {x}')

def linhaA():
    global x, tlock
    espera = random.randint(1, 3)
    time.sleep(espera)
    tlock.acquire()
    try:
        print(f'A linha A recebeu: {x}')
        x += 3
        print(f'Novo valor de x após linha A: {x}')
    finally:
        tlock.release()

def linhaB():
    global x, tlock
    espera = random.randint(1, 3)
    time.sleep(espera)
    tlock.acquire()
    try:
        print(f'A linha B recebeu: {x}')
        x = 2 * x
        print(f'Novo valor de x após linha B: {x}')
    finally:
        tlock.release()

if __name__ == '__main__':
    main()