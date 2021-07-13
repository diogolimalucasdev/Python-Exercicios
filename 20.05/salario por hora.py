print("Descubre o total do salario do funcionario: ")

salario_horas = float(input("Digite o salario por hora: "))

horas_trabalhada= float(input("Horas trabalhada:  "))

total_salario = salario_horas * horas_trabalhada


print(f"O salario bruto é de: {total_salario} ")

inss = total_salario  * 0.08

ir = total_salario * 0.11

sindicato = total_salario * 0.05

salario_final = total_salario - (ir + sindicato + inss)

print(f"O valor do inss é de: {inss}")
print(f"O valor do imposto de renda é de : {ir} ")
print(f" O valor do sindicato é de : {sindicato}")
print(f"O salario Liquido é de : {salario_final}")
print(f"O valor do desconto é de : {(total_salario - salario_final)}")

