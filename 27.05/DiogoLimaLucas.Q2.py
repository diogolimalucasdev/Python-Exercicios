idade = int(input("Digite sua idade:  "))
peso = int(input("Digite seu peso:  "))

#500 mg por ml
#cada ml é 20 gotas ou seja 10 gotas é 250mg e meio ml

mg = 500
gotas = 20

if idade >= 12:
    if peso > 60:
        mg_tomar = 1000 / mg
        gotas_tomar = mg_tomar * 20
        print(f"O usuario devera tomar {gotas_tomar} gotas")
    else:
        mg_tomar = 875 / mg
        gotas_tomar = mg_tomar * 20
        print(f"O usuario devera tomar {gotas_tomar} gotas")

elif idade < 12:
    if peso >= 5 and peso <= 9:
        mg_tomar = 125 * 20
        gotas_tomar = mg_tomar / 500
        print(f"O usuario devera tomar {gotas_tomar} gotas")

    elif peso > 9 and peso <= 16:
        mg_tomar = 250 * 20
        gotas_tomar = mg_tomar / 500
        print(f"O usuario devera tomar {gotas_tomar} gotas")

    elif peso > 16 and peso <= 24:
        mg_tomar = 500 * 20
        gotas_tomar = mg_tomar / 500
        print(f"O usuario devera tomar {gotas_tomar} gotas")

    elif peso > 24:
        mg_tomar = 750 * 20
        gotas_tomar = mg_tomar / 500
        print(f"O usuario devera tomar {gotas_tomar} gotas")

    else:
        print("peso nao ideal para dosagem, ou nao calculado pelo medicamento")

