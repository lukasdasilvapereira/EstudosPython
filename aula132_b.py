import json

from aula132 import caminho_arquivo, Pessoa

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    print(dados)