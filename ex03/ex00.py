# calcular media aritimetica dos numeros fornecidos

def main():
    quantidade = int(input("digite a quantidade: "))
    soma = 0
    contador = 0

    while contador < quantidade:
        soma += float(input("valor: "))
        contador += 1

    media = soma / contador
    print(f"a media dos valores eh: {media:.2f}")


main()
