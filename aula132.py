# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados

import json

caminho_arquivo = 'aula132.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Lucas", 19)
p2 = Pessoa("Luan", 10)
bd = [vars(p1), vars(p2)]

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
