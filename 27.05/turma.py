alunos= int(input("digite quantos alunos tem na turma"))

soma =0
contador = 0

while(contador < alunos):
    nota_aluno = float(input(f"Digite a nota do aluno {contador + 1} :  "))
    soma = soma + nota_aluno
    contador = contador + 1




media = soma / contador
print(f"A média da sala é de {media}")