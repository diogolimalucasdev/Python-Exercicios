login = "adm"
senha = "@SenhaAdm"
sair = "nao"
tentativas = 0

while (tentativas <= 5) and(sair == "nao"):

    tentativas = tentativas + 1

    login2 = input("Digite o login para ter acesso: ")
    senha2 = input("Digite a senha do login: ")

    if(login2 == login) and (senha2 == senha):
        tentativas = tentativas - 1
        continuar = "nao"

        while(continuar == "nao"):
            primeira_nota = int(input("Digite a primeira nota do aluno:  "))
            segunda_nota = int(input("Digite a segunda nota do aluno:  "))

            soma = primeira_nota + segunda_nota
            media = soma / 2
            print(media)

            if(media == 100 or media >= 95):
                print("APROVADO COM DISTINÇÃO...")

            elif(media >= 70 and media < 95 ):
                print("APROVADO...")

            else:
                print("REPROVADO...")

            continuar = input("Deseja sair ?")
            sair = continuar

    elif(senha2 != senha or login2 != login):
        print("Dados Inválidos!")
        print(f"Voce tem mais {6 - (tentativas)} tentativas")


if(tentativas > 5):
    print("Acesso bloqueado!!!")

else:
    print("Notas registrada com sucesso...")