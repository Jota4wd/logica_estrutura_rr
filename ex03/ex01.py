# verifique se um numero n eh primo

def main():
    numero = int(input("escolha o numero: "))

    if eh_primo(numero):
        print("eh primo")
    else:
        print("nao eh primo")


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


main()
