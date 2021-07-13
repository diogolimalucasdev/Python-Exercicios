import math

tamanho_area = float(input("Digite o tamanho da area a ser pintada: "))

litros = float(tamanho_area / 3)
latas = litros / 18

pagamento = 0



if (latas < 1):

    print(f"A area a ser pintada é de: {tamanho_area}m,  serão necessario { litros} litros")
    print(f"que da exatamente {math.ceil(latas)} latas")
    pagamento = 245
    print(f"O pagamento é de {pagamento} R$")
    restante = 18 - litros
    dinheiro = (restante * 245) / 18
    print(f"Sobrao {restante} litros, que são exatamente { dinheiro}R$")

else:

    print(f"A area a ser pintada é de: {tamanho_area}m,  serão necessario {litros} litros")
    print(f"que da exatamente {math.ceil(latas)} latas")
    pagamento = 245 * math.ceil(latas)
    print(f"O pagamento é de {pagamento} R$")
    restante = (math.ceil(latas) * 18) - litros
    dinheiro = (restante * 245)/ 18
    print(f"Sobrao {restante} litros, que são exatamente {dinheiro} R$ ")


