#numa eleição existem 3canditados (a,b,c) elabora umprograma que peça o numero totaldeeleiçõesemumaseção
#peça aracadaeleitor votar eaofinalmostrar o numero de votos de cada candidato
#imprima na tela tambem o percentual relativoa cadacandidato

votosA = 0
votosB = 0
votosC= 0
decisao = 0
votos = 0


while(decisao != "-1"):
    print("Escolha [A] para o candidato A, [B] para o candidato B ou [C] para o candidato C")
    decisao = input("Escolha:  ")

    if(decisao =="-1"):
        break

    while (decisao != "A" and decisao != "a" and decisao != "B" and decisao != "b" and decisao != "C" and decisao != "c"):
        print("Nao exite esse candidato, escolha novamente")
        print("Escolha [A] para o candidato A, [B] para o candidato B ou [C] para o candidato C")
        decisao = input("Escolha:  ")

    if decisao == "A" or decisao == "a":
        votosA = votosA + 1
        print("Voto confirmado")

    if decisao =="B" or decisao == "b":
        votosB = votosB + 1
        print("Voto confirmado")

    if decisao == "C" or decisao == "c":
        votosC = votosC + 1
        print("Voto confirmado")



    votos = votos + 1

print(f"Foram realizados {votos } votos ao total")

porcentagemA = (votosA * 100) / votos
porcentagemB = (votosB * 100) / votos
porcentagemC = (votosC * 100) / votos
print(f"O candidato A recebeu {votosA} votos, {porcentagemA}% dos votos totais")
print(f"O candidato B rcebeu {votosB} votos, {porcentagemB}% dos votos totais")
print(f"O candidato C recebeu {votosC} votos, {porcentagemC}% dos votos totais")
