# calcule o valor liguido de um salario dada tambem as aliquotas dos impostos sobre o valor bruto

def main():
    bruto = float(input("valor do salario bruto: "))
    aliquota = float(input("valor do assalto(%): ")) / 100

    liquido = bruto - imposto_eh_roubo(bruto, aliquota)

    print(f"depois do assalto te sobrou {liquido:.2f}, mas ainda irao te assaltar no consumo do que sobrou")


def imposto_eh_roubo(salario, aliquota):
    return salario * aliquota

main()
