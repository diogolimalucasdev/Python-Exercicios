#vamos criar uma lista com nossas banda favoritas. Essa lista vai se chamar inicialmante nula banda = []
#crie um programa qpergunte se o usuario deseja adicionar uma nova banda na listaou exibir  a lista

bandas = []

while True:
    adiconar = int(input( " Para adicionar uma banda digite[1]\n para exibir as bandas favoritas digite[2] "
                          "\n para sair digite [3]\n --->: "))

    if adiconar == 1:
        banda = input("Digite o nome da banda: ")
        bandas.append(banda)

    elif adiconar == 3:
        break
    else:
        if len(bandas) <= 0:
            banda = input("Digite pelo menos o nome de uma banda:   ")
            bandas.append(banda)
            print(bandas)
        else:
            print(bandas)

