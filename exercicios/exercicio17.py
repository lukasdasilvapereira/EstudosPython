try:
    n1 = (input("Digite um número: "))
    conversao = int(n1)
    print(f"Seu número está convertido em int número = {n1} {type(conversao)}")
except Exception as error:
    print(error)
finally:
    print("Programa finalizado")