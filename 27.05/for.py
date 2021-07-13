soma = 0
contador = 0
for i in range(1, 500):
    if i % 3 == 0:
        print(i)
        soma = soma + i
        contador =contador + 1

print(f"A soma dos valores no intervalo de 1 a 500 é de:{soma}")
print(f"quantidade de numeros multiplos de 3: {contador}")