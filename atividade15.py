senha = input("Digite a senha secreta: ")

if senha == "python":
    print("Acesso liberado!")
elif senha == "PYTHON":
    print("Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas.")
else:
    print("Senha incorreta!")