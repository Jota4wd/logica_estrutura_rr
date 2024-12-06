# nao eh exatamente um exercicio, mas outro exemplo q achei interessante manter

import os
import random

def main():
    vet = list(range(1, 101))
    target = random.choice(vet)

    user_try = user_search(target)
    binary_try = binary_search(vet, target)

    print(f"\nhumano fez {user_try} tentativas.")
    print(f"maquina fez {binary_try} tentativas.")

    if user_try < binary_try:
        print('parabens venceu a maquina neo')
    else:
        print('jamais ira superar a maquina neo')



def user_search(alvo):
    chute = 0
    palpites = 0
    os.system("clear")

    while chute != alvo:
        chute = int(input("chuta ai: "))
        palpites += 1

        if chute < alvo:
            print("mais alto")
        else:
            print("mais baixo")

    return palpites


def binary_search(lista, valor):
    start = 0
    end = len(lista) - 1
    tentativas = 0

    while start <= end:
        tentativas += 1
        meio = (start + end) // 2

        if lista[meio] == valor:
            return tentativas
        elif lista[meio] < valor:
            start = meio + 1
        else:
            end = meio - 1

    return tentativas


if __name__ == "__main__":
    main()
