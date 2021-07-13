print("Calcular o valor do carro alugado pelo usuario ")

valor_km = float(input("Digite quanto a empresa cobra por km rodado:"))
km = float(input("digite quantos km foi pecorrido com esse carro:  ")) * valor_km

valor_dias = int(input("Digite quanto a empresa cobra por dia: "))
dias = float(input("Digite quantos dias o usuario ficou com o carro: ")) * valor_dias

valor = km + dias

print("O valor a ser pago pelo usuario é de : ", valor, "R$")