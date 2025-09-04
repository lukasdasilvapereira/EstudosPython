horario = input("Tudo bem? Pode me dizer o horário? ")

try:
    horario_int = int(horario)
    if horario_int > 13 and horario_int < 19:
        print("Boa tarde")
    elif horario_int >= 19:
        print("Boa noite")
    else:
        print("Bom dia")
except:
    print("Digite um número válido")