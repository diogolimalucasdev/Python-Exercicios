lista1 = []
lista2 = []

lista_junta = []

for x in range(0,11):
    elemento = int(input(f"Digite um numero para posição {x} na lista1: "))
    lista1.append(elemento)


for x in range(0,11):
    elemento = int(input(f"Digite um numero para posição {x} na lista2: "))
    lista2.append(elemento)


lista1.sort()

lista2.sort()
print(lista1)
print(lista2)
for x in range(0,11):
    lista_junta.append(lista1[x])
    lista_junta.append(lista2[x])

print(lista_junta)