# calcula as raizes de uma equaçao de segundo grau (que tenha raizes reais)

import math

def main():
    # solicita os coeficientes ao usuario
    a = float(input("digite o coeficiente a (nao pode ser 0): "))
    b = float(input("digite o coeficiente b: "))
    c = float(input("digite o coeficiente c: "))

    delta = b*b - 4 * a * c

    # verifica se as raizes sao reais
    if delta < 0:
        return "nao existem raizes reais."

    elif delta == 0:
        raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
        print(f"a equaçao soh possui uma raiz: {raiz}")

    else:
        raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
        print(f"as raizes sao: {raiz1}, {raiz2}")


main()
