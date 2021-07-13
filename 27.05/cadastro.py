print("                                                CADASTRO                ")

nome = input("Digite seu nome:  ")
idade = int(input("Digite Sua idade:  "))
salario = float(input("Digite o salario: "))
sexo = input("Escolha seu gênero [F] ou [M]:  ")


estado_civil = input("Escolha [S] pra solteiro, [C] pra casado, [V] pra viuvo [D] pra divorciado:  ")


while (len(nome) <= 3):
    print("Escrava um nome com mais de 3 caracteres...")
    nome = input("Digite seu nome:  ")

while (idade <= 0 ) or (idade > 90):
    print("Sua idade deve estar entre 1 e 90 anos...")
    idade = int(input("Digite Sua idade:  "))
while salario <= 0:
    print("Digite um salario válido...")
    salario = float(input("Digite o salario:  "))

while (sexo != "f") and (sexo != "F") and (sexo != "M") and (sexo != "m"):
    print("Digite um dos gêneros...")
    sexo = input("Escolha seu gênero [F] ou [M]:  ")

while (estado_civil != "s") and (estado_civil != "c") and (estado_civil != "v") and (estado_civil != "d")\
    and (estado_civil != "S") and (estado_civil != "C") and (estado_civil != "V") and (estado_civil != "D"):
    print("Escolha um estado civil válidoo...")
    estado_civil = input("Escolha [S] pra solteiro, [C] pra casado, [V] pra viuvo  e [D] pra divorciado:  ")

print("    #               Cadastro concluído...          #          ")
