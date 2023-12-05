import re
from math import sqrt, floor, ceil

tiempos = [int(x) for x in re.findall(r"\d+", input())]
distancias = [int(x) for x in re.findall(r"\d+", input())]

producto_posibilidades = 1

for t, d in zip(tiempos, distancias):
    # La distancia que alcanza el bote, si x es el tiempo que se mantiene
    # el pulsador es x*(x+t). Si se quiere que sea mayor que de, entonces
    # x*(x+t) > d, es decir, -x^2 + xt - d > 0, de donde se obtiene que
    # (t - sqrt(t^2 -4d)/2 < x < (t + sqrt(t^2 -4d)/2

    lim_inferior = (t - sqrt(t*t - 4*d)) / 2
    lim_superior = (t + sqrt(t*t - 4*d)) / 2

    # Número de enteros entre los límites
    posibilidades = int(ceil(lim_superior) - floor(lim_inferior) - 1)

    producto_posibilidades *= posibilidades

print(producto_posibilidades)