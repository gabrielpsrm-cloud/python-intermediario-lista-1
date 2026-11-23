print("=== TAVERNA DO DRAGÃO ===")

# Passo 1 - Senha secreta
senha = input("Digite a senha secreta para entrar: ")

if senha == "dragao123":

    print("Entrada liberada!")

    # Passo 2 - Verificação da idade
    idade = int(input("Digite sua idade: "))

    if idade < 13:
        print("Você ganhou um suco de uva!")
    else:
        print("Você ganhou uma Poção Mágica!")

    # Passo 3 - Escolha do item pela personalidade
    print("\n=== ESCOLHA SEU ITEM ===")
    print("1 - Espada")
    print("2 - Escudo")
    print("3 - Arco")

    opcao = int(input("Escolha seu item: "))

    if opcao == 1:
        item = "Espada"
        preco = 50
    elif opcao == 2:
        item = "Escudo"
        preco = 30
    elif opcao == 3:
        item = "Arco"
        preco = 40
    else:
        item = ""
        preco = 0
        print("Opção inválida!")

    # Passo 4 - Calculadora de mesada
    if preco > 0:
        ouro = float(input("Quanto ouro você possui? "))

        if ouro >= preco:
            troco = ouro - preco
            print(f"Você comprou um(a) {item}!")
            print(f"Seu troco é de {troco:.2f} moedas.")
        else:
            falta = preco - ouro
            print(f"Você não tem ouro suficiente!")
            print(f"Faltam {falta:.2f} moedas.")

else:
    print("Senha incorreta! A entrada está bloqueada.")