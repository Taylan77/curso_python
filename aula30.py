"""
CONSTANTE = "Variaveis" que nao vao mudar 
Muitas condiçoes no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # Velocidade atual do carro
local_carro = 99 # Local em que o carro esta na estrada

RADAR_1 = 60 # Velocidade maxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) 

carro_multado = carro_passou_radar_1 and vel_carro_radar_1

if velocidade > RADAR_1:
    print('Voce passou acima da velocidade permitida!!')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado:
    print('Voce foi multado!')