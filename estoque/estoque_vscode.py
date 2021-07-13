import os
import time
# produtos
produtos = {
    "diodo": [0, 0],
    "resistor": [0, 0],
    "capacior": [0, 0]
}
produtos_numero = {
    "1": [0, 0],  # isso representa o diodo
    "2": [0, 0],    #isso representa o resistor
    "3": [0, 0]  #isso representa o capacitor

}
def adicionar(dicio, chave, index, valor_novo):
    dicio[chave] [index] = valor_novo
    #acesso o dicionario e modifico o a lista
    print(dicio)
    return dicio



print("Controle de estoque ")
time.sleep(3)
os.system('cls')

while True:
    controle = int(input("Digite [1] para entrada de produto e [2] para sáida: "))
    time.sleep(3)
    os.system('cls')
   # print('\n' * 100)


    if controle == 1:
        print("Escolha...")
        print("Irá adicionar um novo produto, digite [1]")
        print("Irá adicionar itens ao um produto ja existente, digite [2] ")
        time.sleep(3)
        os.system('cls')

        controle_entrada = int(input("Escolha [1] ou [2] ou [3]\n"))
        os.system('cls')
    
        while(controle_entrada):
        #Fiz isso para que quando o usuario digitar algum item que nao tem ele possa voltar e criar

            if controle_entrada == 1:
                print("Entrada de um novo produto ou itens ...")

                nome_do_produto = input("Escreva o nome do produto que ira adicionar ao estoque: ")
                if nome_do_produto in produtos:
                    print("encontrei")
                # verifico se o que foi digitado esta dentro do meu dicionario


            elif controle_entrada == 2:

                print("Entrada de itens...")
                nome_do_produto= input("Selecione o nome ou numero do produto que voce ira adicionar: ")

                if nome_do_produto in produtos:
                    # verifico se o que foi digitado esta dentro do meu dicionario
                    print("achei o produto!")

                    qtd = int(input(f"Digite a quantidade de itens que serao adicionados ao componente {nome_do_produto}"))
                    adicionar(produtos,nome_do_produto, 0, qtd)

                    novo_elemento = int(input("Deseja adicionar mais um elemento? se sim digite [1], se nao deseja digite [2]"))

                    if (novo_elemento == 1):
                        # para que o usuario possa criar um item se o que ele tentou adicionar item nao tinha na lista
                        controle_entrada = 1

                    else:
                        print("Ok!")
                        break

                else:
                    print("Não encontrei nenhum componente com esse nome, deseja criar?")
                    novo_elemento = int(input("Se sim digite [1], se nao deseja digite [2]"))

                    if(novo_elemento == 1):
                        #para que o usuario possa cirar um item se o que ele tentou adicionar item nao tinha na lista
                        controle_entrada = 1

                    else:
                        print("Ok!")
                        break



        else:
            print("tratamento de erro")
        # aqui seria um tratamento de erro

    elif controle == 2:
        print("Saida de produto ou de itens... ")

    else:
        print("tratamento de erro")
    # aqui so caso ele escolha erra fazer com que apresente um erro e volte la pra condição
