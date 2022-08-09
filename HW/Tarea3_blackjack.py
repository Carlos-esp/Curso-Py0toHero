#Simulación de un juego de blackjack con 2 mazos
import numpy as np

mazo=["A",1,2,3,4,5,6,7,8,9,10,"J","Q","K"]*4

def jugar_blackj(mazo, num_mazo):
    mazo_tot=mazo*num_mazo
    cartas=np.random.choice(mazo_tot,size=4,replace=False)
    print(f'Las cartas elegidas son: {cartas}')
    for i,j in enumerate(cartas):
        if j in ["J","Q","K"]:
            cartas[i]=10
        elif j in ["A"]:
            cartas[i]=1
        else:
            cartas[i]=int(j)
    cartas=cartas.astype(int)
    mano_jug=cartas[[0,2]]
    mano_casa=cartas[[1,3]]
    puntos_jug=sum(mano_jug)
    puntos_casa=sum(mano_casa)
    print(f'La mano del jugador es {mano_jug}, puntos totales: {puntos_jug}')
    print(f'La mano de la casa es {mano_casa}, puntos totales: {puntos_casa}')
    if puntos_jug>puntos_casa:
        ganador="El jugador"
    elif puntos_jug<puntos_casa:
        ganador="La casa"
    else:
        ganador="Empate"
    print(f'EL ganador: {ganador}')
    return ganador


jugar_blackj(mazo,2)