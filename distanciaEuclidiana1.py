import math

def distanciaEuclidiana(x_1, y_1, x_2, y_2):
    distancia = math.sqrt( abs(x_1 - x_2)**2 + abs(y_1 - y_2)**2 )
    return distancia