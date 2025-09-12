# EMPACOTAMENTO E DESEMPACOTAMENTO DE DICIONÁRIOS

pessoa = {
    "nome": 'Lucas',
    "sobrenome": "Pereira",
}

dados_pessoa = {
    "idade": 19,
    "altura": 1.7
}

pessoa_completa = {**pessoa, **dados_pessoa} # VAI JUNTAR OS DOIS

print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostrar(*args, **kwargs):
    for name, valor in kwargs.items():
        print(name, valor)


mostrar(nome="Joana", idade=19)

