mesada = float(input("Quanto dinheiro você tem guardado? R$ "))
preco = float(input("Qual o preço do jogo? R$ "))

if mesada >= preco:
    troco = mesada - preco
    print(f"Compra realizada! Seu troco é R$ {troco:.2f}")
else:
    falta = preco - mesada
    print(f"Faltam R$ {falta:.2f} para comprar o jogo.")