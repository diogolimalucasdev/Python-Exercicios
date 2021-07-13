x= 1
#enquanto x for igual a 1 execute todo o codigo

while(x == 1):

    print("Descubrase se seu peso esta dentro do padrão saudavel")

    altura = float(input("Digite sua altura: "))

    sexo = input("Digite seu gênero: [F] ou [M]: ")

    peso = float(input("Digite seu peso: "))

    if (sexo == "M") or (sexo == "m") or (sexo == "F") or(sexo == "f"):
        if (sexo == "F") or (sexo == "f"):
            peso_ideal= (62.1 * altura) - 44.7

        elif (sexo == "M") or (sexo == "m"):
            peso_ideal= ((72.7 * altura) - 58)


        if(peso > peso_ideal):
            print(f"Voce esta acima do peso ideal para seu genero, o peso ideal seria {peso_ideal}")

        elif(peso == peso_ideal):
            print("Voce esta com o peso ideal para seu genero.")
        else:
            print(f"Voce esta abaixo do peso ideal, o peso ideal seria {peso_ideal}")

    else:
        print("Dados Invalidos, tente outra vez.")


    op = input("pressiona 's' para continuar ou 'n' para sair")

    if(op == "n"):
        x = 0

        print("Volte sempre...")






