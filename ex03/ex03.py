# jogo do adivinha, biblioteca random, i hate rng hu3

import os
import random

def main():

    random.seed()
    alvo = random.randint(1, 99)
    chute = 0
    palpites = 0
    os.system("clear")

    while chute != alvo:
        chute = int(input("chuta ai: "))
        palpites += 1

        if chute == alvo:
            print(f"acertou em {palpites}")
        elif chute < alvo:
            print("mais alto")
        else:
            print("mais baixo")


main()
