numero = int(input("Digite um numero e descubra o fatorial dele:  "))

resultado = 1
contador = 1
while (contador <= numero):
    print(f"{resultado} x {contador} = ")
    resultado = resultado * contador
    contador += 1
    print(f"{resultado} ")


resultado = 1
contador = 1

for x in range(numero, 1, -1):
    resultado *= x
    print(resultado)