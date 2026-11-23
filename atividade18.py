tesouro = float(input("Digite o valor do seu tesouro: "))

if tesouro > 1000:
    imposto = tesouro * 0.10
    total = tesouro - imposto

    print(f"Imposto cobrado: {imposto:.2f} moedas")
    print(f"Tesouro após o imposto: {total:.2f} moedas")
else:
    print("Você não precisa pagar imposto!")