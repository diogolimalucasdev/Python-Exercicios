novos_produtos = {
}

novos_produtos["item"] = [0,0,0]
print(novos_produtos)

novos_produtos["item"] [0] = 10
print(novos_produtos)



def adicionar(dicio, chave, index, valor_novo):
    dicio[chave] [index] = valor_novo
    print(dicio)

adicionar(novos_produtos,"item", 1, 10)
