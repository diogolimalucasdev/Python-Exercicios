# Um empresario expandiu seus negócios e agora possui uma loja de conveniencias.
# Voce foi requisitado para elaborar um programa que implemente uma caixa
# registradora no estabelecimento. O programa deverá receber um numero
# desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador do caixa para indicar o
# final da compra (encerrar o programa). O programa deve então mostrar o total
# da compra e perguntar o valor em dinheiro que o cliente forneceu, para
# então calcular e mostrar o valor do troco que deve ser realizado.
# Após esta operação, o programa deverá voltar ao ponto inicial,
# para atender e registrar a próxima compra.

valorCaixa = 0
compra = 1
lista_compra = []
while compra != 0:
    print("Nova compra")
    print("Para encerrar a compra do cliente atual digite 0 no valor do produto...")
    compra = 1
    lista_compra = []
    contagem = 0
    while compra != 0:
        contagem = contagem + 1
        item = float(input(f"Digite o valor do produto {contagem}º: "))

        if item == 0:
            break
        lista_compra.append(item)

    valor_compra = sum(lista_compra)

    print(f"O valor total da compra ficou: {round(valor_compra)}R$")

    pagamento = float(input("Valor do pagamento do cliente: "))

    troco = pagamento - valor_compra

    if troco >= 0:
        print(f"Valor do troco: {round(troco)}R$")
        print("Compra finalizada, agradecemos...")

    else:
        print(f"Esta faltando: {round(troco)}R$")
        pagamento2 = float(input("Pague o valor restante:  "))
        troco2 = troco + pagamento2
        print(troco2)
        if troco2 < 0:
            print("Compra cancelada!!!")
            valor_compra = 0

    valorCaixa = valor_compra + valorCaixa

    compra = int(input("Digite [1] para registrar uma nova compra e [0] para fechar o caixa..."))

print(f"Valor do caixa: {valorCaixa}R$")
