# mais um implementado apenas pela curiosidade, talvez seja o mais proximo de um backtracking

import os

# Limpa a tela (funciona em sistemas Unix)
os.system('clear')

def mover(origem, destino):
    obj = origem.pop()
    destino.append(obj)
    print('___________')
    print(f'1: {h1}')
    print(f'2: {h2}')
    print(f'3: {h3}')

def hanoi(n, origem, destino, tmp):
    if n == 1:
        mover(origem, destino)
    else:
        hanoi(n - 1, origem, tmp, destino)
        mover(origem, destino)
        hanoi(n - 1, tmp, destino, origem)

# Solicita a quantidade de anéis ao usuário
x = int(input('Quantidade de anéis: '))
h1 = []
h2 = []
h3 = []

# Preenche a haste 1 com os anéis
for i in range(x, 0, -1):
    h1.append(i)

# Exibe o estado inicial das hastes
print('1:', h1)
print('2:', h2)
print('3:', h3)

# Inicia o processo de resolução da Torre de Hanoi
hanoi(x, h1, h3, h2)
