equipamentos = []
valores = []
seriais = []
departamentos = []
condiçao = "SIM"

while condiçao == "SIM":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero serial: ")))
    departamentos.append(input("Departamento: "))
    condiçao = input("Digite 'sim' para continuar: ").upper()
print(equipamentos)
print(valores)
print(seriais)
busca = input("Digite o nomedo equipameto que seja buscar: ")

for indice in range(0, len(equipamentos)):
    print(indice)
    if busca == equipamentos[indice]:
        print("Valor.. ", valores[indice])
        print("Serial..", seriais[indice])