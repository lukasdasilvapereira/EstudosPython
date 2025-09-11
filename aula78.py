# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    "nome": 'Lucas',
    "sobrenome": 'Pereira'
}

pessoa.setdefault("idade", None)

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get("nome")) # O GET VEM COM NONE AUTOMATICAMENTE CASO A CHAVE NÃO EXISTIR

pessoa.update(nome="Luquinha", idade=19)

eliminar = pessoa.pop()
ultima_chave = pessoa.popitem()

##for chave in pessoa:
    ##print(chave) # VAI RETORNAR O NOME DAS CHAVES
