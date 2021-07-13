decisao = 0
while(decisao != 5):
    n1 = float(input("Digite um numero:  "))
    n2 = float(input("Digite o segundo numero: "))

    print("[1] Somar os numeros")
    print("[2] Multiplicar os numeros")
    print("[3] Subtrair os numeros")
    print("[4] Dividir os numeros")
    print("[5] para sair do programa")

    decisao = int(input("Escolha: "))

    if decisao == 1:
        conta = n1 + n2
        print(f"{n1} + {n2} = {conta}")

    elif decisao == 2:
        conta = n1 * n2
        print(f"{n1} * {n2} = {conta}")

    elif decisao == 3:
        conta = n1 - n2
        print(f" {n1} - {n2} = {conta}")

    elif decisao == 4:

        if n2 == 0:
            print("Nao existe divisao por zero")

        else:
            conta = n1 / n2
            print(f" {n1} / {n2} = {conta}")


    decisao = int(input("Deseja sair ? [5] para sair e [0] para continuar"))

print("Programa finalizado...")