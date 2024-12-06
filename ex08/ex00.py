def main():
    lista = [29, 10, 14, 37, 13]
    print("Lista original:", lista)

    bubble_sort = BubbleSort(lista.copy())
    bubble_sort.ordenar()
    print("Lista ordenada com Bubble Sort:", bubble_sort.lista)

    insertion_sort = InsertionSort(lista.copy())
    insertion_sort.ordenar()
    print("Lista ordenada com Insertion Sort:", insertion_sort.lista)


class Ordenadora:
    def __init__(self, lista):
        self.lista = lista

    def ordenar(self):
        pass


class BubbleSort(Ordenadora):
    def ordenar(self):
        n = len(self.lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.lista[j] > self.lista[j+1]:
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]


class InsertionSort(Ordenadora):
    def ordenar(self):
        for i in range(1, len(self.lista)):
            key = self.lista[i]
            j = i - 1
            while j >= 0 and key < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1
            self.lista[j + 1] = key



if __name__ == '__main__':
    main()
