import random
import math

def estimar_area_quarto_circulo(num_pontos, raio):
    pontos_dentro = 0

    for _ in range(num_pontos):
        # Gerar coordenadas aleatórias dentro do quadrado que circunscreve o círculo
        x = random.uniform(0, raio)
        y = random.uniform(0, raio)

        # Verificar se o ponto está dentro do quarto de círculo
        if x**2 + y**2 <= raio**2:
            pontos_dentro += 1

    # Estimar a área do quarto de círculo
    area_estimada = (4 * pontos_dentro) / num_pontos * (raio**2)
    return area_estimada

# Função principal
def main():
    # Solicitar ao usuário o raio do círculo
    raio = float(input("Digite o raio do círculo: "))
    # Solicitar ao usuário o número de pontos
    num_pontos = int(input("Digite o número de pontos a serem gerados: "))
    
    # Calcular a área estimada
    area = estimar_area_quarto_circulo(num_pontos, raio)
    print(f"A área estimada do círculo com raio {raio} é: {area}")

# Executar a função principal
if __name__ == "__main__":
    main()
