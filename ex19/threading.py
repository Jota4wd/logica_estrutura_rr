import threading

class Mpar(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print('Thread em execução na classe Mpar')

def main():
    print('Criando um novo thread')
    obj = Mpar()
    print('Iniciando a execução do thread')
    obj.start()
    obj.join()
    print('Fim do principal')

if __name__ == "__main__":
    main()