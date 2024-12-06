# mais um q soh deixei salvo pq achei bem interessante a forma que foi feito o fatorial de arranjo

import os
os.system('clear')

def permutacoes(lista):
    if len(lista) == 1: #caso base
        return [lista]

    primeiro =  lista[0]
    resto = lista[1:]
    resultado = []

    for perm in permutacoes(resto):
        for i in range(len(perm) + 1):
            resultado = resultado + [perm[:i] + [primeiro] + perm[i:]]

    return resultado

x = input('Digite a lista (ex: 1, 2, 3): ')
lista = x.split(',')  # Divide a string em uma lista
lista = [item.strip() for item in lista]  # Remove espaços em branco

print(permutacoes(lista))
