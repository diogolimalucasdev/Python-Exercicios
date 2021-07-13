nota = float(input("Insira uma nota de 0 a 10...: "))



# or é ou
while(nota < 0) or (nota > 10) :
    nota = float(input("A nota nao pode ser inferior a 0 ou superior a 10...: "))

print("Obrigado Nota válida...")