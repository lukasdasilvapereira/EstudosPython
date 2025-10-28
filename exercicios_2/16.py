class Contexto:
    def __enter__(self):
        print("Iniciando...")
        return "To dentro do enter"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo....")

with Contexto() as f:
    print(f)


class List:
    def __enter__(self):
        lista = []
        return lista
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass

with List() as l:
    l.append("Pão")
    l.append("Suco")
    print(l)
    print("Foram adicionadas", len(l), "itens")