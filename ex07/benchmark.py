import os
import random
import timeit
import copy
from statistics import mean
from my_insertion import insertion_sort as my_insertion
from my_bubble import bubble_sort as my_bubble
from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from quick_funcional import quick_sort
from quick_inplace import quicksort_inplace
from merge import merge_sort
from shell import shell_sort

def generate_test_case(length):
    return [random.randint(1, length) for _ in range(length)]

def benchmark_sort(sort_func, vector, num_runs=5):
    times = []
    for _ in range(num_runs):
        # Cria uma cópia do vetor para cada teste
        test_vector = copy.deepcopy(vector)

        # Usa timeit para medição mais precisa
        start_time = timeit.default_timer()
        sort_func(test_vector)
        end_time = timeit.default_timer()

        times.append(end_time - start_time)

    return {
        'min': min(times),
        'max': max(times),
        'avg': mean(times)
    }

def main():
    os.system('clear')
    length = int(input('comprimento: '))

    # Gera o vetor original
    original_vector = generate_test_case(length)

    # Define os algoritmos a serem testados
    algorithms = {
        'My Insertion': my_insertion,
        'Insertion': insertion_sort,
        'My Bubble': my_bubble,
        'Bubble': bubble_sort,
        'Merge': merge_sort,
        'Selection': selection_sort,
        'Shell': shell_sort,
        'Quick Funcional': quick_sort,
        'Quick Inplace': quicksort_inplace
    }

    # Executa os testes e armazena os resultados
    results = {}
    for name, func in algorithms.items():
        results[name] = benchmark_sort(func, original_vector)

    # Imprime os resultados ordenados por tempo médio
    print(f"\nResultados para vetor de tamanho {length}:")
    print(f"{'Algorithm':<15} {'Min (s)':<12} {'Avg (s)':<12} {'Max (s)':<12}")
    print("-" * 51)

    sorted_results = sorted(results.items(), key=lambda x: x[1]['avg'])
    for name, times in sorted_results:
        print(f"{name:<15} {times['min']:<12.6f} {times['avg']:<12.6f} {times['max']:<12.6f}")

if __name__ == '__main__':
    main()
