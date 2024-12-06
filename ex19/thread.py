import threading
import time

def main():
    thread1 = threading.Thread(target=funcao_linha_execucao_separada, args=('linha1', 5, 1))
    thread1.start()

    try:
        time.sleep(3)
        print('\nThread principal ainda em execução')
    except KeyboardInterrupt:
        print('Thread principal interrompida...')

def funcao_linha_execucao_separada(nome, contador, tempo):
    print(f'eu sou... {nome}')
    for i in range(1, contador + 1):
        print(f'{nome}: contador = {i}')
        time.sleep(tempo)
    print(f'\nThread {nome} finalizada\n')

if __name__ == '__main__':
    main()