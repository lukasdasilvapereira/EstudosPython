# Use lambda para ordenar pela idade

pessoas = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("David", 22)]

l1 = sorted(pessoas, key=lambda item: item[1])

print(l1)