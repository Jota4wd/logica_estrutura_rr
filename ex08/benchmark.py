import time

from sorts import bubble_encadeada, insertion_encadeada

class Aluno:
    def __init__(self, nome='', endereco='', email=''):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.proximo = None

# Criar lista encadeada de alunos para ordenar
primeiro = Aluno("Alice", "Rua A", "alice@example.com")
primeiro.proximo = Aluno("Bob", "Rua B", "bob@example.com")
primeiro.proximo.proximo = Aluno("Charlie", "Rua C", "charlie@example.com")

# Medir o tempo de execução do bubble sort
inicio_bubble = time.time()
bubble_sorted = bubble_encadeada(primeiro)
fim_bubble = time.time()
tempo_bubble = fim_bubble - inicio_bubble

# Medir o tempo de execução do insertion sort
inicio_insertion = time.time()
insertion_sorted = insertion_encadeada(primeiro)
fim_insertion = time.time()
tempo_insertion = fim_insertion - inicio_insertion

print("Lista ordenada com Bubble Sort:")
atual = bubble_sorted
while atual is not None:
    print(atual)
    atual = atual.proximo

print("\nTempo de execução do Bubble Sort:", tempo_bubble, "segundos")

print("\nLista ordenada com Insertion Sort:")
atual = insertion_sorted
while atual is not None:
    print(atual)
    atual = atual.proximo

print("\nTempo de execução do Insertion Sort:", tempo_insertion, "segundos")
