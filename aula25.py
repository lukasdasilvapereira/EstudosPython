nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

contem_espaco = " " in nome

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome contém ou não espaços? {contem_espaco}")
    print(f'Seu nome tem {len(nome)} letras')
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Você deixou campos vazios")
