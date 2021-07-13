lista = []
for qtd in range(0, 3):
    lista.append(float(input(f"Digite um numero na posição {qtd + 1}: ")))


lista.sort()

print("O maior numero é: ", lista[2])
print("O menor numero é: ", lista[0])