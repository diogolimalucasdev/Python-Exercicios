# valida e corrija o numero de telefone
# faça um programa que leia um numero de telefone, via telcado, e corrija o numero caso deste somente 7 digitios,
# acrescentando o "3" na frente deste numero


condição = 1

while condição == 1:
    tipo_numero = int(input("Se for celular digite [1] e fixo [2]:  "))
    dd = input("Digite o DD: ")
    numero = input("Digite o numero do telefone: ")
    quantidade = len(numero)
    falta = 8 - quantidade
    numero_formatado = "3" * falta + numero


    if tipo_numero == 1:
        quantidade = len(numero)
        falta = 8 - quantidade
        numero_formatado = "3" * falta + numero
        if quantidade < 9:
            print("(" + dd + ")", "9" + numero_formatado[0:4] + "-" + numero_formatado[4:8])
        else:
            if numero[0] == "9":
                print("Numero ja esta no padrão de 9 algarismos...")
                print("(" + dd + ")", numero_formatado[0:4] + "-" + numero_formatado[4:9])
            else:
                print("(" + dd + ")", "9" + numero[0:4] + "-" + numero[4:8])


    else:
        if quantidade < 8:
            print("(" + dd + ")", numero_formatado[0:4] + "-" + numero_formatado[4:8])
        else:
            print("Numero ja esta no padrão de 8 algarismos...")
            print("(" + dd + ")", numero[0:4] + "-" + numero[4:8])

    condição = int(input("Para adicionar outro numero digite [1] se nao digite [2]"))
