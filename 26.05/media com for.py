soma_notas = 0
media = 0

qtd_alunos = int(input("Digite o numero de alunos: "))

for qtd in range(0, qtd_alunos):
    nota = float(input(f"Digite a primeira nota do aluno de numero {qtd + 1}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno de numero {qtd + 1}: "))
    media = float((nota + nota2) / 2)
    print(f"A media do aluno {qtd + 1}º é de: {media}")

    soma_notas = media + soma_notas
    media = soma_notas/qtd_alunos

print(f"A média da sala é: {media}")
