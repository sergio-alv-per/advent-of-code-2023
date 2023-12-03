from sys import stdin
import re

encontrar_numeros = re.compile(r"(\d+)")

encontrar_engranajes = re.compile(r"\*")

def añadir_numeros_en_linea(linea, numeros, inicio, fin, inicio_extendido, fin_extendido):
    for nmatch in encontrar_numeros.finditer(linea[inicio_extendido:fin_extendido]):
        if nmatch.end()+inicio_extendido >= inicio and nmatch.start()+inicio_extendido <= fin:
            numeros.append(int(nmatch.group(1)))
            if len(numeros) == 2:
                break

def suma_ratios_engranajes(lineas):
    linea_superior = lineas[0]
    linea_medio = lineas[1]
    linea_inferior = lineas[2]

    suma_ratios = 0

    for match in encontrar_engranajes.finditer(linea_medio):
        inicio = match.start()
        fin = match.end()

        inicio_extendido = max(0, inicio - 3)
        fin_extendido = min(len(linea_superior), fin + 3)

        numeros = []
        añadir_numeros_en_linea(linea_superior, numeros, inicio, fin, inicio_extendido, fin_extendido)       
        añadir_numeros_en_linea(linea_medio, numeros, inicio, fin, inicio_extendido, fin_extendido)
        añadir_numeros_en_linea(linea_inferior, numeros, inicio, fin, inicio_extendido, fin_extendido)
        
        assert len(numeros) < 3

        if len(numeros) == 2:
            suma_ratios += numeros[0] * numeros[1]

    return suma_ratios

lineas = []
suma = 0

for i, line in enumerate(map(str.strip, stdin)):
    if i == 0:
        lineas.append("." * len(line))
        lineas.append(line)
    else:
        if i > 1:
            lineas.pop(0)
        
        lineas.append(line)

        suma += suma_ratios_engranajes(lineas)

lineas.pop(0)
lineas.append("." * len(line))
suma += suma_ratios_engranajes(lineas)

print(suma)
