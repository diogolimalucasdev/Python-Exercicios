#escalen  tds diferentes
#isosceles dois lados iguais
#equialatero tds lados iguais


print("Digite o valor de cada lado de um triangulo e descubra que tipo ele é...")


lado1 = int(input("Digite o primeiro lado:  "))

lado2 = int(input("Digite o segundo lado:  "))

lado3 = int(input("Digite o terceiro lado:  "))


if((lado1 + lado2 ) > lado3) == True  and ((lado2 + lado3) > lado1) == True and ((lado1 + lado3) > lado2) == True :
    print("Estes valores fazem um triangulo existente")
    ok == True

    if lado1 == lado2 and lado2 == lado3:
        print("esse triangulo é do tipo equilatero...")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Esse triangulo é do tipo isosceles...")

    else:
        print("Esse triangulo é do tipo escaleno...")

else:
    print("Os valores informado nao formam um triangulo...")