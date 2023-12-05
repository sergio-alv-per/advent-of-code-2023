import re
from math import sqrt, floor, ceil

tiempo = re.findall(r"\d[\d ]+", input())[0]
tiempo = tiempo.replace(" ", "")
tiempo = int(tiempo)

distancia = re.findall(r"\d[\d ]+", input())[0]
distancia = distancia.replace(" ", "")
distancia = int(distancia)

lim_inferior = (tiempo - sqrt(tiempo*tiempo - 4*distancia)) / 2
lim_superior = (tiempo + sqrt(tiempo*tiempo - 4*distancia)) / 2

posibilidades = int(ceil(lim_superior) - floor(lim_inferior) - 1)

print(posibilidades)
