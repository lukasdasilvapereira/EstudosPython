# dir, hasattr e getattr em Python

string = "Lucas"

if hasattr(string, "upper"):
    print('Existe upper')
    print(getattr(string, "upper")())
else:
    print("Não existe")
