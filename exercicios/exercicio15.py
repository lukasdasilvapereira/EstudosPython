generator = (n if n % 2 == 0 else " " for n in range(21))

for num in generator:
    print(num)


#2. Quadrados perfeitos

#Crie um generator expression que gere os quadrados dos números de 1 a 10.

gen = (x**2 for x in range(0,10))

for num in range(10):
    for x in gen:
        print(f"{num} = {x}")
        num += 1