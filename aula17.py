"""CONDIÇÃO"""

condicao = True

if condicao:
    print("Este é o código do if")
else:
    print("Este é o else do primeiro if")

if 10 == 10:
    print("Outro if")


print("FORA DO IF")

condicao1 = True

if condicao1:
    pass
elif False:
    ...
elif condicao1:
    ...

# ... e pass podem ser usados pora não resolver o código