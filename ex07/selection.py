# selection sorte

def main():
    length = int(input('quantidade: '))
    vet = []

    while length > 0:

        vet.append(int(input('valor: ')))
        length -= 1

    print(f'original:\n{vet}')
    selection_sort(vet)
    print(f'ordenada:\n{vet}')

def selection_sort(vector):
    for i in range(len(vector)):
        menor = i

        for j in range(i + 1, len(vector)):
            if vector[menor] > vector[j]:
                menor = j

    tmp = vector[i]
    vector[i] = vector[menor]
    vector[menor] = tmp
