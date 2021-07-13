
numero = int(input("Que numero voce quer ver a tabuada ?: "))

vezes =int(input("digite quantas vezes voce quer: "))
#range quer disse: intervalo(intervalo de 0 a 11)
for qtd in range(0, 11):
    print(f"{numero} x {qtd} = {numero * qtd}")
