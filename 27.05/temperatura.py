lista_temperatura = []

for x in range(1, 13):
    mes_temperatura = float(input(f"Digite a temperatura do mes {x}: "))

    lista_temperatura.append(mes_temperatura)

for i in range(0, 12):
    print(f"temperatura do mes {i+1} = {lista_temperatura[i]}")

soma = sum(lista_temperatura)

media = soma / 12

print(f"A media anual é de: {media}")

