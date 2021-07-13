numero = 0
contadorN = 0
contadorP = 0
contador = 0
print("Parasair do programa digite o numero negativo 222")
while(numero != -222):
    numero = int(input("Digite um numero: "))
    if(numero == -222):
        break

    if(numero >= 0):
        contadorP = contadorP + 1

    elif(numero < 0 ):
        contadorN = contadorN + 1

    contador = contador + 1

print(f"Total de números informados: {contador}")
print(f"Total de números positivos: {contadorP}")
print(f"Total de números negativos:{contadorN}")