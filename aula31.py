nome = input("Digite seu nome: ")
nome_str = str(nome)

if len(nome_str) <= 4:
    print("Seu nome é curto")
elif len(nome_str) == 5 or len(nome_str) == 6:
    print("Seu nome é normal")
else:
    print("Seu nome é gigante")