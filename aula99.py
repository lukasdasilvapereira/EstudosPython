# TRY, EXCEPT, ELSE E FINALLY

try:
    print("ABRIU O PROGRAMA")
    print(123)
except Exception as error:
    print(error)
else:
    print("Não deu erro")
finally:
    print("FECHOU O PROGRAMA")

# O FINALLY VAI SEMPRE SER EXECUTADO
# O ELSE N TEM MUITA UTILIDADE, MAS É USADO CASO N TENHA ERROS