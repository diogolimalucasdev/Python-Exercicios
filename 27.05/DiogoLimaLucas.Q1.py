
decisao = 1
while(decisao == 1):
    nome = input("Digite seu nome:  ")
    cpf = int(input("Digite seu CPF:  "))
    renda = float(input("Digite sua renda mensal:  "))

    dependentes = input("Possui dependentes(filhos, esposa)? Responda sim ou nao:  ")

    if ((dependentes == "SIM") or (dependentes =="sim")):
        dependentesQauntidade = int(input("digites quantos dependentes: "))
        desconto = (0.05 * dependentesQauntidade) * renda
        renda_final = renda - desconto
        print(f"Com o valor do desconto de{desconto}R$, a renda liquida ficou {renda_final}R$")

    else:
        print(f"Sem desconto...")



    if (renda <= 2200):

        print(f"O portador do cpf: ({cpf}) esta Isento de imposto por ter uma renda inferior a 2200R$")

    if(renda > 2200 or renda <= 5500):
        valorPagar = renda * 0.10
        print(f"O portador do cpf: ({cpf}) tera que pagar 10% da renda. Valor a ser pago {valorPagar}R$")


    elif(renda > 5500 or renda <= 7700):
        valorPagar = renda * 0.15
        print(f"O portador do cpf: ({cpf}) tera que pagar 15% da renda. Valor a ser pago {valorPagar}R$")

    else:
        valorPagar = renda * 0.20
        print(f"O portador do cpf ({cpf}) tera que pagar 20% da renda. Valor a ser pago {valorPagar}R$")


    decisao = int(input("Deseja adicionar mais um usuario? se SIm digite [1] ou se NAO digite [2]"))