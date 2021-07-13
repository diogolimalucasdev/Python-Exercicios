# em uma compeitção de salto em distancia cada atleta tem direita a 5 saltos, No final da serie de saltos de cada
# atleta, o melhor e o pior resultafossao eliminados.

saltos = []
nome = "a"
while nome != "":
    nome = input("Insira o nome do atleta: ")
    if nome == "":
        break
    for i in range(0, 5):
        salto = float(input(f"Insira o valor do salto {i + 1}:  "))
        saltos.append(salto)

    maior = max(saltos)
    menor = min(saltos)
    print(f"Maior salto {maior}")
    print(f"Menor salto {menor}")
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))

    print("Saltos para contagem da média...")
    for x in range(0, 3):
        print(saltos[x])

    media = sum(saltos) / len(saltos)
    print(f"Media dos saltos válidos: {round(media, 2)}")

print("Programa encerrado...")
