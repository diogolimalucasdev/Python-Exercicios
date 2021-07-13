temperatura = 0

temperaturas = []

print("para sair digite a temperatura = 99")

while (temperatura != 99):

    temperatura = float(input("Digite a temperatura atual: "))

    if temperatura == 99:
        break


    else:
        temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
maior_temperatura = max(temperaturas)

menor_temperatura = min(temperaturas)

print(f"A maior temperatura é {maior_temperatura}")
print(f"A menor Temperatura é {menor_temperatura}")
print(f"A media de Temperatura é {media}")
