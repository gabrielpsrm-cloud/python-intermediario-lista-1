mesada = float(input("Digite o valor da mesada: "))
nota = input("Você tirou nota A em matemática? ")

if nota.lower() == "sim":
    total = mesada + 20
else:
    total = mesada

print(f"Sua mesada final é: R$ {total:.2f}")