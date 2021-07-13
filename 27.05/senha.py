print("Faça seu cadastro...")
login = input("Digite seu login: ")
senha = int(input("Digite sua senha:  "))

print("Cadastro Concluido...")

tentativas = 0


while(tentativas < 4):
   login2 = input("Digite seu login: ")
   senha2 = int(input("Digite a senha: "))
   if(senha2 == senha and login2 == login ):
      #faço isso pq eu fujo da condição de limite que é 4
      tentativas = 5
,
   else:
      print("Senha incorreta!")
      #ja aqui o limite dele é 4
      tentativas = tentativas + 1

if tentativas == 4:
   print("Numero de tentativas excetidas, acesso bloqueado!")

else:
   print("Acesso permitido")