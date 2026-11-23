print("=== CHAPÉU SELETOR ===")
print("1 - Livros")
print("2 - Esportes")
print("3 - Natureza")
print("4 - Pegadinhas")

opcao = int(input("Qual você prefere? "))

if opcao == 1:
    print("Corvinal!")
elif opcao == 2:
    print("Grifinória!")
elif opcao == 3:
    print("Lufa-Lufa!")
elif opcao == 4:
    print("Sonserina!")
else:
    print("Hmm, escolha inválida. O Chapéu está confuso!")