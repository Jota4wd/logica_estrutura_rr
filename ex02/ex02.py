# calcule a area de um circulo, retangulo, triangulo, etc

def main():
    print("Cálculo de Áreas de Figuras Geométricas")

    # Círculo
    r = float(input("Digite o raio do círculo: "))
    print(f"A área do círculo é: {area_circulo(r)}")

    # Retângulo
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    print(f"A área do retângulo é: {area_retangulo(base, altura)}")

    # Triângulo
    base_tri = float(input("Digite a base do triângulo: "))
    altura_tri = float(input("Digite a altura do triângulo: "))
    print(f"A área do triângulo é: {area_triangulo(base_tri, altura_tri)}")

    # Quadrado
    lado = float(input("Digite o lado do quadrado: "))
    print(f"A área do quadrado é: {area_quadrado(lado)}")

    # Trapézio
    base1 = float(input("Digite a base 1 do trapézio: "))
    base2 = float(input("Digite a base 2 do trapézio: "))
    altura_trap = float(input("Digite a altura do trapézio: "))
    print(f"A área do trapézio é: {area_trapezio(base1, base2, altura_trap)}")


def area_circulo(raio):
    # Calcula a área do círculo
    return 3.14159 * (raio ** 2)


def area_retangulo(base, altura):
    # Calcula a área do retângulo
    return base * altura


def area_triangulo(base, altura):
    # Calcula a área do triângulo
    return (base * altura) / 2


def area_quadrado(lado):
    # Calcula a área do quadrado
    return lado ** 2


def area_trapezio(base1, base2, altura):
    # Calcula a área do trapézio
    return (base1 + base2) * altura / 2


main()
