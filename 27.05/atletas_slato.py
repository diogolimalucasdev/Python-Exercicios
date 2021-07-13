
while True:
    nome = input("Digite o nome do atleta:  ")
    if nome == "":
        break
    controle = 0
    saltos_list = []

    for i in range(controle, 5):
        salto = float(input(f"Digite a distancia do salto {i + 1}:  "))
        saltos_list.append(salto)

        controle += 1

    media = (sum(saltos_list) / 5)
    print(f"Todos os saltos do atleta {nome} foram esses:"
          f" {saltos_list[0], saltos_list[1], saltos_list[2], saltos_list[3], saltos_list[4]}")
    print(f"A media dos saltos do atleta {nome} foi de {media}")


print("Programa encerrado...")
