print("=== FEIRA DE POÇÕES ===")
print("1 - Poção de Vida: R$ 10")
print("2 - Poção de Força: R$ 20")
print("3 - Poção de Magia: R$ 30")

opcao = int(input("Escolha uma poção: "))

if opcao == 1:
    print("Você escolheu a Poção de Vida. Valor: R$ 10")
elif opcao == 2:
    print("Você escolheu a Poção de Força. Valor: R$ 20")
elif opcao == 3:
    print("Você escolheu a Poção de Magia. Valor: R$ 30")
else:
    print("Opção inválida!")