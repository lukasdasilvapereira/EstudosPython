tarefas = []
tarefas_refazer = []
print("Comandos: listar, desfazer, refazer")
lista_code = input("Digite uma tarefa ou comando: ")
tarefas.append(lista_code)

while lista_code != 'sair':
    tarefas_refazer = []
    print()
    print("TAREFAS:", tarefas)
    print()
    print("Comandos: listar, desfazer, refazer")
    lista_code = input("Digite uma tarefa ou comando: ")
    tarefas.append(lista_code)
    if lista_code == 'listar':
        print(tarefas)
    elif lista_code == 'desfazer':
        tarefa = tarefas.pop()
        tarefas_refazer.append(tarefa)
        print(tarefas)
    elif lista_code == 'refazer':
        tarefas_refazer.pop() += tarefas
        print(tarefas)
    elif lista_code == 'desfazer' and tarefas == '':
        print("Nada a desfazer")
    elif lista_code == 'refazer' and tarefas == '':
        print("Nada a refazer")
    else:
        ...

