import math

decisao = 0
while(decisao == 0):
    a = int(input("Digite um valor para 'a'"))
    if (a == 0):
        break
    b = int(input("Digite um valor para 'b'"))
    c = int(input("Digite um valor para 'c'"))

    delta = (b * b) - (4 * a * c)
    print(delta)

    if delta < 0:
        print("A equação não possui raizes reais.")
        break
    elif delta == 0:
        #sqrt é raiz, eu importo a biblioteca math, utilizo a função sqrt encima de delta
        raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
        print("A equacao possui apenas uma raiz real ", raiz)
    elif delta > 0:
        x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        x2 = (-1 * b - math.sqrt(delta)) / (2 * a)
        print("As raizes da equacao sao ", x1, "e", x2)

    decisao = int(input("Deseja continuar realizar outra?: "))