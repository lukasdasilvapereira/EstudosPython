# Sets - Conjuntos em python (tipo set)
# Sets são eficientes para remover valores duplicados de iteráveis
# Não aceitam valores mutáveis 
# Seus valores serão sempre únicos
# Não tem índexes
# Não garantem ordem
# São iteráveis (for, in, not in)

s1 = {1, 2, 3, 4}
print(s1)
print(3 in s1)

for numero in s1:
    print(numero)

# TRANSFORMANDO LISTA EM SET

l1 = [5, 6, 7, 7 , 7]

s2 = set(l1)

print(s2)

# MÉTODOS ÚTEIS NO SETS

# add, update, clear, discard

s11 = set()
s11.add("Lucas")
s11.update("Olá mundo")
#s11.clear()
s11.discard("Olá mundo") # VAI DESCARTAR
print(s11)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s20 = {1, 2, 3}
s30 = {2, 3, 4}
s40 = s20 | s30 # Vai unir os dois sets
s40 = s20 & s30 # Vai mostrar os que estão presentes nos dois sets
s40 = s20 - s30 # Vai mostrar o set que está na esquerda e não está em nenhum outro lugar
s40 = s20 ^ s30 # Vai mostrar os itens que só existem nos próprios sets
print(s40)