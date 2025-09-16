def classificar_dado(dado):

    if isinstance(dado, int):
        return "Isso é um Inteiro"

    elif isinstance(dado, float):
        return "Isso é um Flutuante"
    
    elif isinstance(dado, str):
        return "Isso é uma String"
    
    elif isinstance(dado, list):
        return "Isso é uma Lista"

    else:
        return "OUTRO TIPO"


print(classificar_dado(20))
print(classificar_dado(1.2))
print(classificar_dado([0, 1, 2]))
print(classificar_dado(True))
print(classificar_dado("Olá"))
print(classificar_dado(False))
        
    
    
