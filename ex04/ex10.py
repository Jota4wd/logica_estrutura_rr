# nao eh um exercicio real, apenas um exemplo q achei curioso de numeros primos

import os
os.system('clear')

limite = int(input('limite: '))

for numero in range(2, limite):
    for x in range(2, numero):
        if numero % x == 0:
            print(f'{numero} igual a {x} X {numero // x}')
            break

    else:
        print(f'{numero} eh um numero primo')
