# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# decoradores são açúcar sintático, ou seja podemos usar o @ e o nome da função que tá decorando encima da função que é pra ser decorada, assim podemos copiar ela

def decoradora(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"O resultado é {resultado}")
        print("Você foi decorada")
        return resultado
    return interna

@decoradora
def inverter_string(string):
    print(f'{inverter_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError("Precisa ser string")

invertida = inverter_string('123')
print(invertida)