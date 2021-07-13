numero1 = int(input("digite um numero inteiro: "))

numero2 = int(input("digite outro numero inteiro: "))


soma = numero1 + numero2

print("A soma dos numeros é: ", soma)


if ( soma >= 10):
    print("Numero é maior que 10")


elif(soma <= 0):
    print("O numero é menor que 0")

else:
    print("numero nao é maior que 10")