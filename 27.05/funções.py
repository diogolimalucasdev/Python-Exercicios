def preencherIventario(lista):
    condição = "SIM"
    while condição == "SIM":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Numero do serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        condição = input("Dogote 'sim' para continuar: ").upper()


def exibirIventario(lista):
    for elemento in lista:
        #o elemnto pega o valor de uma lista que esta dentro de uma lista principal
        #por isso eu posso determinar os indices
        print(lista)
        print(elemento)
        print(f"Nome = {elemento[0]}")
        print(f"Valor = {elemento[1]}")
        print(f"Serial = {elemento[2]}")
        print(f"Departamento = {elemento[3]}")




