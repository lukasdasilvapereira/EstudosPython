# TRY, EXCEPT, ELSE E FINALLY

try:
    a = 18
    b = 0
    c = a / b

#except ZeroDivisionError as error:
    #print(error)

#except (TypeError, IndexError) as error: # DUAS EXCEÇÕES JUNTAS
    #print(error)

except Exception as erro: # TODOS OS ERROS
    print(erro)


