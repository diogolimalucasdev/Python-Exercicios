gabarito = []

for a in range(10):
    print(f"Questao {a + 1}")
    resposta_certa = gabarito.append(input("Informe alternativa correta: "))

condição = 1
nota = 0
todas_notas = []
while condição == 1:
    print("Digite as respostas de cada questao da prova a seguir...")
    nota = 0
    for i in range(0, 10):
        questao = input(f"Digite a reposta da questão {i + 1}: ")

        if questao == gabarito[i]:
            nota = nota + 1
            print(f"Voce acertou...")
        else:
            print("Resposta errada...")

    todas_notas.append(nota)

    print(f"A nota desse aluno é de {nota}")
    condição = int(input("Para verificar mais um aluno digite [1] e para sair digite [0]:  "))

maior_nota = max(todas_notas)
menor_nota = min(todas_notas)

media = sum(todas_notas) / len(todas_notas)

print(f"A maior nota foi a {maior_nota}")
print(f"A menor nota foi a {menor_nota}")
print(f"A media das notas da turma foi {media}")

print("Gabarito da prova")
for x in range(0, 10):
    print(f"Questao {x + 1} resposta {gabarito[x]}")
