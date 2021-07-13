acumulador = 0
quantidade = 0
notas_aluno = []
nota = 0
while(nota != -1):
    nota = float(input(f"Digite a nota do aluno{quantidade + 1 }: "))
    quantidade += 1
    if nota > 0:
        notas_aluno.append(nota)




print(f"Foram cadastradas {quantidade -1 } notas")
print(f"Notas em ordem que fora castrada{notas_aluno}")
print(f"Notas em ordem inversa que foram cadastrada {notas_aluno[::-1]}")

print(f"Soma das notas = {sum(notas_aluno)}")


media = sum(notas_aluno) / (quantidade -1)
print(f"Media das notas {media}")

lista = len(notas_aluno)
while(0 <= lista):
    for i in range(0, lista):
        verificar = notas_aluno[i]
        if verificar > media:
            print("Nota acima da média")
            print(notas_aluno[i])

        lista -= 1





