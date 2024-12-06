import os

os.system('clear')
quant = int(input('Quantidade da série: '))
soma = 0
denominador = 1

for i in range(quant):
    if i % 2 == 0:
        soma += 1 / denominador
    else:
        soma -= 1 / denominador
    denominador += 2

pi = 4 * soma
print(f'O valor aproximado de pi com {quant} termos é: {pi}')
