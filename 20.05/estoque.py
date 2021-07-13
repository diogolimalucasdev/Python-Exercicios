# produtos

diodo = 0
resistor = 0
capacitor = 0
placas_pcd = 0
placas_velhas = 0
ampola = 0
led = 0

print("Controle de estoque ")

while True:
    controle = int(input("Digite [1] para entrada de produto e [2] para sáida: "))
    if controle == 1:
        print("Escolha...")
        print("Irá adicionar um novo produto, digite [1]")
        print("Irá adicionar itens ao um porduto ja existente, digite [2]")

        controle_entrada = int(input("Escolha [1] ou [2]"))

        if controle_entrada == 1:
            print("Entrada de um novo produto ou itens ...")
            novo_produto = input("Escreva o nome do produto que ira adicionar ao estoque: ")



        elif controle_entrada == 2:
            print("Entrada de itens...")
            produto = input("Selecione o nome ou numero do produto que voce ira adicionar: ")
            # nao sei se o python tem dicionario
            # queria colocar um condição para que verificar se o porduto existe na lista ou nao

        else:
            print("tratamento de erro")
        # aqui seria um tratamento de erro

    elif controle == 2:
        print("Saida de produto ou de itens... ")

    else:
        print("tratamento de erro")
# aqui so caso ele escolha erra fazer com que apresente um erro e volte la pra condição
