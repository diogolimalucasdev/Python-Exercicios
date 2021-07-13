#foi feita uma estatistica em 5 cidades brasileiras pra coletar dados
#sobre acidentes de transito. Foram obtidos os seguintesdados:
#Codigo da cidade>;
#Numero de veiculos de passeio;
#Numero de acidentes de transito com vitimas;
#Desejas-se saber;
#Qual omaior e menor indice de acidentes de transito e a que cidade pertence
#Qual a media de veiculos nas 5 cidade juntas.
quantidade = 1
cidades = 5

maiorAcidente = 0
menorAcidente = 0
somaVeiculos = 0
somaAcidentes = 0

while (quantidade <= cidades):
    print("  ")
    cidade = input("Digite o codigo da cidade: ")
    veiculos = int(input("Digite o numero de veiculos de passeio da cidade: "))
    acidentes = int(input("Digite o numero  de acidentes de transito com vitimas: "))

    somaVeiculos = veiculos + somaVeiculos
    somaAcidentes = acidentes + somaAcidentes


    if acidentes > maiorAcidente:
        maiorAcidente = acidentes
        maiorAcidentecidade = cidade

    if quantidade == 1:
        menorAcidente = acidentes

    if menorAcidente > acidentes:
        menorAcidente = acidentes
        menorAcidenteCidade = cidade


    quantidade += 1

    print( " ")


mediaVeiculos = somaVeiculos / cidades
mediaAcidentes = somaAcidentes /cidades

print(f"A soma deveiculo das 5 cidades é de {somaVeiculos} ")
print(f"A soma de acidentes das 5 cidades é de {somaAcidentes}")
print(f"A cidade com maior indice de acidente é {maiorAcidentecidade} com {maiorAcidente} acidentes")
print(f"A cidade com menor indice de acidente é {menorAcidenteCidade} com {menorAcidente} acidentes")
print(f"A media de veiculos da 5 Cidades são {mediaVeiculos}")
print(f"A media de acidentes das 5 cidades são {mediaAcidentes}")