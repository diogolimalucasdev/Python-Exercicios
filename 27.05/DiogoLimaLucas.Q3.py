peso = 0
pessoas = 0
decisao = 0
acumulador = 0
while(decisao == 0):
    print(f"pessoas {pessoas}")


    if (peso > 420):
        print(f"Peso limite execidido!!!!, peso atual: {peso}")
        peso_sair = int(input("SAIA ALGUEM E INFORME O PESO QUE SAIU!!!:   "))
        peso = peso - peso_sair
        pessoas -= 1

    elif(pessoas >= 6):
        print("LIMITE DE PESSSOAS EXECIDIDO")
        pessoas_sair = int(input("Digite [1] quando sair alguem!!!"))
        if pessoas_sair == 1:
            pessoas -= 1

    elif(pessoas <= 6 and peso <= 420):
        print("elevador liberado para uso")
        acumulador = int(input("Informe seu peso: "))
        peso = peso + acumulador
        pessoas = pessoas + 1




