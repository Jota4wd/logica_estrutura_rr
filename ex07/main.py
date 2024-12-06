import os
import random
import copy
from datetime import datetime
from my_insertion import insertion_sort as my_insertion
from my_bubble import bubble_sort as my_bubble
from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from quick_funcional import quick_sort
from quick_inplace import quicksort_inplace
from merge import merge_sort
from shell import shell_sort

os.system('clear')

def main():
    length = int(input('comprimento: '))
    vector = []

    i = 0
    while i < length:
        nbr = random.randint(1, length)
        if nbr not in vector:
            vector.append(nbr)
            i += 1

    v_my_i = copy.deepcopy(vector)
    v_my_b = copy.deepcopy(vector)
    v_selection = copy.deepcopy(vector)
    v_insertion = copy.deepcopy(vector)
    v_quick_funcional = copy.deepcopy(vector)
    v_quick_inplace = copy.deepcopy(vector)
    v_merge = copy.deepcopy(vector)
    v_bubble = copy.deepcopy(vector)
    v_shell = copy.deepcopy(vector)

    print(f'original\n{vector}')

    inicio = datetime.now()
    my_insertion(v_my_i)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'my_insertion: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    insertion_sort(v_insertion)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'insertion: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    my_bubble(v_my_b)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'my_bubble: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    bubble_sort(v_bubble)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'bubble: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    merge_sort(v_merge)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'merge: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    selection_sort(v_selection)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'selection: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    shell_sort(v_shell)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'shell: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    v_quick_new = quick_sort(v_quick_funcional)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'quick funcional: {tempo.total_seconds():.6f}')

    inicio = datetime.now()
    quicksort_inplace(v_quick_inplace)
    fim = datetime.now()
    tempo = fim - inicio
    print(f'quick in place: {tempo.total_seconds():.6f}')

if __name__ == '__main__':
    main()
