from sys import stdin
import re

total = 0

NO_SIMBOLOS = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

encontrar_numeros = re.compile(r"(\d+)")

def suma_numeros_linea_medio(lineas):
    linea_superior = lineas[0]
    linea_medio = lineas[1]
    linea_inferior = lineas[2]

    suma_numeros_con_simbolo_adyacente = 0

    for match in encontrar_numeros.finditer(linea_medio):
        numero = int(match.group(1))
        
        inicio = match.start()
        fin = match.end()

        inicio_adyacente = max(0, inicio - 1)
        fin_adyacente = min(len(linea_superior), fin + 1)

        if (set(linea_superior[inicio_adyacente:fin_adyacente]) - NO_SIMBOLOS or
           set(linea_inferior[inicio_adyacente:fin_adyacente]) - NO_SIMBOLOS or
           inicio > 0 and linea_medio[inicio - 1] not in NO_SIMBOLOS or
           fin < len(linea_medio) and linea_medio[fin] not in NO_SIMBOLOS):
            suma_numeros_con_simbolo_adyacente += numero
    
    return suma_numeros_con_simbolo_adyacente


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

        suma += suma_numeros_linea_medio(lineas)

lineas.pop(0)
lineas.append("." * len(line))
suma += suma_numeros_linea_medio(lineas)

print(suma)
