# EXERCÍCIOS DE SISTEMA DE PERGUNTAS E RESPOSTAS

perguntas = [
    {
        "pergunta": "Quanto é 2 + 2?",
        "opcoes": ['1', '2', '3', '4'],
        'resposta': '4',
    },
    {
        "pergunta": "Quanto é 5 * 5?",
        "opcoes": ['10', '15', '25', '30'],
        'resposta': '25',
    },
    {
        "pergunta": "Quanto é 10/2?",
        "opcoes": ['1', '5', '4', '2'],
        'resposta': '5',
    },
]

acertos = 0
erros = 0


for loop in perguntas:
    print(loop['pergunta'])
    for i, valor in enumerate(loop['opcoes'], start=1):
        print(f"({i}) {valor}")
        i = loop["resposta"]
    respondeu = input("Qual a resposta? ")

    if respondeu.isdigit():
        indice = int(respondeu) - 1
        if loop['opcoes'][indice] == loop['resposta']:
            print()
            print("ACERTOOOOUUUU!!!")
            print()
            acertos += 1
        else:
            
            if respondeu == loop['resposta']:
                print()
                print("ACERTOOOOUUUU!!!")
                print()
                acertos += 1

    else:
        print()
        print("ERROUUU! Mais sorte da próxima vez..")
        print()
        erros += 1


print(f"Obrigado por participar!! Você teve o total de {acertos} acertos e {erros} erros")

