cor = input("Escolha uma cor (Azul, Amarelo ou Vermelho): ")

if cor.lower() == "azul":
    print("Você está calmo!")
elif cor.lower() == "amarelo":
    print("Você está feliz!")
elif cor.lower() == "vermelho":
    print("Você está zangado!")
else:
    print("Cor inválida!")