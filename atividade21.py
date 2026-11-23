print("=== CHAPÉU SELETOR ===")
print("1 - Livros")
print("2 - Esportes")
print("3 - Natureza")
print("4 - Pegadinhas")

opcao = int(input("Qual você prefere? "))

if opcao == 1:
    print("Você pertence à Corvinal!")
elif opcao == 2:
    print("Você pertence à Grifinória!")
elif opcao == 3:
    print("Você pertence à Lufa-Lufa!")
elif opcao == 4:
    print("Você pertence à Sonserina!")
else:
    print("Escolha inválida!")