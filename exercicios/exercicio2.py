# Exercício 2: Variáveis e Tipos de Dados
# 1. Crie uma variável chamada 'nome' com seu nome.
# 2. Crie uma variável chamada 'idade' com sua idade.
# 3. Crie uma variável chamada 'altura' com sua altura (pode ser float, ex: 1.75).
# 4. Imprima o tipo de cada variável.
# 5. Imprima uma frase usando todas as variáveis, como "Olá, meu nome é [nome], tenho [idade] anos e minha altura é [altura] metros."

nome = "Lucas"
idade = 19
altura = 1.70

print(type(nome), type(idade), type(altura))

print(f'Olá meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros')