idade = 0
idades = []

while(idade != -10):
    idade = int(input("Informe sua idade:  "))
    idades.append(idade)


media = sum(idades) / len(idades)
print(media)

if media > 0 and media <= 25:
    print("Turma jovem")

elif media > 25 and media <= 60:
    print("Turma adulta")

else:
    print("Turma idosa")