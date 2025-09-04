# CONSTANTE = "Váriaveis" que não mudam
# if muito grande deixa o código feio

velocidade = 90
km = 90


# CONSTANTES MAIUSCULAS
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velo_carro_pass_radar_1 = velocidade > RADAR_1

if velo_carro_pass_radar_1:
    print("Desacelere!! Você ultrapassou o limite")


if km >= (LOCAL_1 - RADAR_RANGE) and \
    km <= (LOCAL_1 + RADAR_RANGE) and \
        velo_carro_pass_radar_1:
    print("Carro multado em radar 1")

# \ faz com que possamos terminar o código na outra linha
