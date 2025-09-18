# VERIFICADOR DE IDADE

def verificar(idade):
    if idade < 18:
        raise ValueError("Você não tem no mínimo 18 anos")
    else:
        return "Acesso Permitido"

edad = verificar(17)

print(edad)
