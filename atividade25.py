idade = int(input("Digite sua idade: "))
animal = input("Você prefere gatos ou cachorros? ")

if idade < 18:
    if animal.lower() == "gatos":
        print("Você é jovem e prefere gatos!")
    elif animal.lower() == "cachorros":
        print("Você é jovem e prefere cachorros!")
    else:
        print("Animal inválido!")
else:
    if animal.lower() == "gatos":
        print("Você é adulto e prefere gatos!")
    elif animal.lower() == "cachorros":
        print("Você é adulto e prefere cachorros!")
    else:
        print("Animal inválido!")