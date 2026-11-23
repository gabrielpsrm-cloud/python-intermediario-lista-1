print("=== ESCOLHA SUA CLASSE ===")
print("1 - Atacar de longe")
print("2 - Atacar de perto")

opcao = input("Escolha seu estilo de combate: ")

if opcao == "1":
    arma = input("Magia (A) ou Arco (B)? ")

    if arma.upper() == "A":
        print("Sua classe é Mago!")
    elif arma.upper() == "B":
        print("Sua classe é Arqueiro!")
    else:
        print("Opção inválida!")

elif opcao == "2":
    arma = input("Espada (A) ou Adagas (B)? ")

    if arma.upper() == "A":
        print("Sua classe é Guerreiro!")
    elif arma.upper() == "B":
        print("Sua classe é Assassino!")
    else:
        print("Opção inválida!")

else:
    print("Opção inválida!")