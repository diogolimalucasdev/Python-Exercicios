#façaum programa qeue calcule o numero medio de alunos por turma de uma escola.Para isso,peça aquantidade deturma e
# e a quantidade de alunos para cada turma.As turmas nao podem ter mais de 40alunos.

turmas = int(input("Digite o numero de turmas:  "))


alunos_turmas = []

for i in range(0, turmas):
    alunos = int(input(f"Na turma {i + 1} tem quantos alunos?:  "))
    while alunos > 40:
        print("Numero superior ao limite...")
        alunos = int(input(f"Na turma {i + 1} tem quantos alunos?:  "))
    alunos_turmas.append(alunos)


print(alunos_turmas)
media =  (sum(alunos_turmas) / len(alunos_turmas))

print(f"A media de alunos por tumar é de: {media}")

