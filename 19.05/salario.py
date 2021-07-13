salario = float(input("Digite o valor do salario: "))

aumento = float(input("informe o porcentual de aumento do funcionario: "))

salario_final = (salario * (aumento / 100)) + salario

print("salario do funcionario agora é de: ", salario_final, "o aumento foi de", aumento,"%")


print("os", aumento,"% equivale a: ", salario_final - salario, "R$")