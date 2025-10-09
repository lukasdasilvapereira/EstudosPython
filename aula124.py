import json

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input("Digite uma tarefa ou comando: ")

    if tarefa == 'sair':
        break

    if tarefa == 'listar':
        print()
        if not tarefas:
            print("Nenhuma tarefa adicionada")
        else:
            print("TAREFAS", tarefas)
            print()
    elif tarefa == 'desfazer':
        if not tarefas:
            print("Nada a desfazer")
        else:
            ultima = tarefas.pop()
            tarefas_refazer.append(ultima)
            print()
            print("TAREFAS", tarefas)
            print()
    elif tarefa == 'refazer':
        if not tarefas:
            print("Nada a refazer")
        else:
            ultima = tarefas_refazer.pop()
            tarefas.append(ultima)
            print()
            print("TAREFAS", tarefas)
            print()
    else:
        tarefas.append(tarefa)
        tarefas_refazer.clear()
        print()
        print("TAREFAS", tarefas)
        print()

with open('aula124.json', 'w', encoding='utf8') as arquivo:
    json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)


with open('aula124.json', 'r', encoding='utf8') as arquivo:
    working = json.load(arquivo)
    print(working)



