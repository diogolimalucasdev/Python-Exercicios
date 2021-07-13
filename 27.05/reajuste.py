salario = float(input("Digite o salario atual do funcionario: "))

print("Reajuste da empresa... \n ")
print("Abaixo de 550R$ ... 15%")
print("De 500R$ até 1000R$ ... 10%")
print("Acima de 1000R$ ... 5%")

if salario < 500:
    aumento = salario * 0.15
    salario_final = aumento + salario
    print(f"salario anteior: {salario}")
    print(f"O aumento foi de 15%:({aumento})e o valor final do salario ficou  {salario_final} R$")

elif salario > 500 and salario <= 1000 :
    aumento = salario * 0.10
    salario_final = aumento + salario
    print(f"salario anteior: {salario}")
    print(f"O aumento foi de 10%:({aumento}) e o valor final do salario ficou {salario_final}R$")
else:
    aumento = salario * 0.05
    salario_final = aumento + salario
    print(f"salario anteior: {salario}")
    print(f"O aumento  foi de 5%:({aumento}R$) e o valor final do salario ficou {salario_final}R$")
