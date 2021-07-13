
cliente_10 = int(input("O cliente tem vinculo com a loja a mais de 10 anos? [1] para sim e [2] para não:  "))
idade = int(input("Digite a idade do cliente: "))



valor_compra = float(input("Digite o valor da compra: "))
parcela_compra = int(input("Digite em quantas vezes o pagamento sera realizado: "))


#pagamento a vista desconto de 10%
if parcela_compra == 1:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
   #teste print(valor_final)

    #mais que 5000 R$ desconto de 5%
    if valor_compra > 5000:
        desconto2 = valor_final * 0.05
        valor_final2 = valor_final - desconto2
        # testeprint(valor_final2)

        if cliente_10 == 1:
            desconto3 = valor_final2 * 0.05
            valor_final3 = valor_final2 - desconto3
           #teste  print(valor_final3)


            if idade > 60:
                desconto4 = valor_final3 * 0.05
                valor_final4 = valor_final3 - desconto
                print(f"Pagamento a vista, 10 anos de "
                      f"loja e idade maior que 60 anos, valor do desconto{desconto4 + desconto3 + desconto2 + desconto}")
                print(f"valor final: {valor_final4}")
            else:
                print(f"Pagamento a vista, 10 anos de loja e idademenor que 60 anos,"
                      f" valor de desconto {desconto3 + desconto2 +desconto}")
                print(f"Valor final: {valor_final3}")
        else:
            if idade > 60:
                desconto3 - valor_final2 * 0.05
                valor_final3 = valor_final2 - desconto3
                print(f"Nao é cliente a mais de 10 anos, mas idade superior a 60 anos,"
                      f" valor do desconto{desconto3 + desconto2 + desconto}")
                print(f"Valor final de: {valor_final3}")
            else:
                print(f"Não é cliente a mais de 10 anos, nem tem iidadesuperior a 60 anos,"
                      f" valor do desconto{desconto2 + desconto}")
                print(f"Valor final de: {valor_final2}")


    #nao é mais 5000 mas foi a vista
    else:
        #cliente a mais de 10 anos e foi a vista
        if cliente_10  == 1:
            desconto2 = valor_compra * 0.05
            valor_final2 = valor_compra - desconto2
            print(valor_final2)

            #cliente a mais de 10 anos e foi a vista e tem mais de 60 anos
            if idade > 60:
                desconto3 = valor_final2 * 0.05
                valor_final3 = valor_final2 - desconto
                print("pagamento a vista \n")
                print(f"Cliente com idade superior a 60 anos e  com mais de 10 anos de loja,"
                      f" desconto de{desconto3 + desconto2}")
                print(valor_final3)

            else:
                print(f"cliente com mais de 10 anos de loja, e pagamento a vista, desconto de {desconto2 + desconto}")
                print(valor_final2)
        #Não é cliente a mais de 10 anos mas foi a vista
        else:
            #tem idade mais de 60 anos e foi a vista
            if idade > 60:
                desconto2 = valor_final * 0.05
                valor_final2 = valor_final - desconto
                print(f"cliente com idade superior a 60 anos, pagamento a vista, desconto de {desconto2 + desconto}")
                print(valor_final2)


            else:
                print(f"Pagamento a vista, desconto de {desconto} ")
                print(valor_final)


#parcelado ate 6 vezes
elif parcela_compra > 1 and parcela_compra <= 6:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto


    #compra acima de 5000
    if valor_compra > 5000:
        desconto2 = valor_final * 0.05
        valor_final2 = valor_final - desconto2


            #clientemaisde 10 anos, compra acimade 5000 mas foi parcelado ate 6x
        if cliente_10 > 10:
                desconto3 = valor_final2 * 0.05
                valor_final3 = valor_final2 - desconto3

                if idade > 60:
                    desconto4 = valor_final3 * 0.05
                    valor_final4 = valor_final3  - desconto4
                    print(f"Pagamento parcelado,mas valor acima de 5.000R$, idade superior a 60 anos...")
                    print(f"Cliente com mais 10 anos deloja, desconto e {desconto4 + desconto3 +desconto2 + desconto}")
                    print(valor_final4)

                else:
                    print(f"Pagamento parcelado, valor acima de 5.000 R$, clienteda loja a mais de 10 anos...")
                    print(f"Valor do desconto de {desconto3 + desconto2 + desconto}")
                    print(valor_final3)

        else:
            if idade > 60:
                desconto3 = valor_final2 * 0.05
                valor_final3 = valor_final2 - desconto3
                print(f"Pagamento parcelado, idade superior a 60 anos, valor acima de 5.000R$")
                print(f"Nao é cliente da loja a mais de 10 anos, desconto de{desconto3 + desconto2 + desconto}")
                print(valor_final3)
            else:
                print(f"Pagamento parcelado, valor acima de 5.000R$, desconto de {valor_final2}")
                print(valor_final2)


    #compra nao é acima de 5000
    else:
        #mas o cliente tem mais de 10 anos e loja
        if cliente_10 > 10:
            desconto2 = valor_final * 0.05
            valor_final2 = valor_final - desconto2

            if idade > 60:
                desconto3 = valor_final2 * 0.05
                valor_final3 = valor_final2 - desconto3
                print(f"Idade superior a 60 anos, mais de 10 anos de loja, valor inferior a 5.000R$")
                print(f"Desconto de {desconto3 + desconto2 + desconto}")
                print(valor_final3)

            else:
                print(f"Mais de 10 anos de loja, valor nao é superior a 5.000R$, idade inferior a 60 anos ")
                print(f"Desconto de {desconto2 + desconto}")
                print(valor_final2)
        else:
            if idade > 60:
                desconto2 = valor_final * 0.5
                valor_final2 = valor_final - desconto2
                print(f"Pagamento parcelado, valor nao é superior 5.000R$ nao tem10 anos de loja...")
                print(f"Idade superior a 60 anos, desconto de{desconto2 + desconto}")
                print(valor_final2)
            else:
                print(f"Pagamento parcelado, nao tem idade superior a 60 anos e nem 10 anos de loja ")
                print("Valor nao é superior a 5.000R$, sem desconto...")
                print(valor_compra)








else:
    if valor_compra > 5000:
        desconto = valor_compra * 0.05
        valor_final = valor_compra - desconto

        if cliente_10 > 10:
            desconto2 = valor_final * 0.05
            valor_final2 = valor_final - desconto2

            if idade > 60:
                desconto3 = valor_final2 * 0.05
                valor_final3 = valor_final2 - desconto3
        else:

            if idade > 60:
                desconto2 = valor_final * 0.05
                valor_final2 = valor_final - desconto2

            else:

                print(f"Compra superior a 5.000R$, desconto de {desconto}R$")
                print(valor_final)


    else:
        if cliente_10 > 10:
            desconto2 = valor_compra * 0.05
            valor_final = valor_compra - desconto2

            if idade > 60:
                desconto3 = valor_final * 0.05
                valor_final2 = valor_final - desconto3
                print(f"Cliente com mais de 10 anos de loja, com idade superior a 60 anos, desconto de {desconto3}")
                print(valor_final2)
            else:
                print(f"Cliente commais de 10 anos de loja, desconto de {desconto2 }")
                print(valor_final)
        else:
            if idade > 60:
                desconto = valor_compra * 0.05
                valor_final = valor_compra - desconto
                print(f"Cliente com idade superior a 60 anos, desconto de {desconto}")
                print(valor_final)
            else:
                print(f"Voce nao tem direito a desconto...")
                print(valor_compra)