#Em um compteição de ginatisca cadaatleta recebe votos de 7 jurados.A melhor e a ppior nota sao eliminadas.
#A sua nota fica sendo a media dos votos restante. Voce deve fazer um programa que recebeo nome do ginasta e as notas dos
#7 jurados alcaçandas pelo atleta em sua apresentação e depois informe a sua media, conforme a descrição acima
#descartar a melhor e o pior salto e depois calcular a media com as notas restante

continuar = 1
while continuar == 1:
    notasTotais = []
    nome = input("Digite o nome do atleta:  ")

    for i in range(0, 7):
        notas = float(input(f"Digite a nota do {i + 1} jurado:  "))

        notasTotais.append(notas)

    maior = max(notasTotais)
    menor = min(notasTotais)
    print(f"A maior nota do atleta foi: {maior}")
    print(f"A menornota do atleta foi: {menor}")

    notasTotais.remove(max(notasTotais))
    notasTotais.remove(min(notasTotais))

    for x in range(0,4):
        notasValidas = notasTotais[x]
        print(f"Notas do atleta: {notasValidas}")

    media = sum(notasTotais) / len(notasTotais)
    print(f"A media do atleta é: {media}")

    continuar = input("Digite [1] para cadastrar outro atleta e [2] para sair")

 
