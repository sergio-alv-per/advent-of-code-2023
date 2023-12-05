import re

def obtener_rangos_mapa():
    rangos = []
    input() # Ignorar título mapa
    rango = input()
    while rango:
        r = tuple(int(x) for x in rango.split(" "))
        rangos.append(r)
        rango = input()
    
    return sorted(rangos, key=lambda x: x[1])

def encontrar_correspondencia_en_rangos(numero, rangos):
    for rango in rangos:
        inicio_rango_origen = rango[1]
        inicio_rango_destino = rango[0]
        longitud_rango = rango[2]
        if inicio_rango_origen <= numero < inicio_rango_origen+longitud_rango:
            return inicio_rango_destino + (numero - inicio_rango_origen)
    
    return numero

def colapsar_intervalos(intervalos):
    intervalos_colapsados = []
    for inicio, fin in sorted(intervalos):
        if intervalos_colapsados and intervalos_colapsados[-1][1] >= inicio:
            intervalos_colapsados[-1][1] = max(intervalos_colapsados[-1][1], fin)
        else:
            intervalos_colapsados.append([inicio, fin])
    
    return intervalos_colapsados

def aplicar_rango_a_numero(numero, rango):
    """Se asume que el número está dentro del rango."""
    return rango[0] + (numero - rango[1])

def aplicar_rangos_a_intervalo(intervalo, rangos):
    # LÍMITES SUPERIORES EXCLUSIVOS
    intervalos_resultantes = []

    lim_inferior_intervalo = intervalo[0]
    lim_superior_intervalo = intervalo[1]

    rangos = sorted(rangos, key=lambda x: x[1])

    for rango in rangos:
        inicio_rango_origen = rango[1]
        inicio_rango_destino = rango[0]
        longitud_rango = rango[2]
        fin_rango_origen = inicio_rango_origen + longitud_rango

        if lim_inferior_intervalo < inicio_rango_origen:
            if lim_superior_intervalo <= inicio_rango_origen:
                # CASO 4
                intervalos_resultantes.append((lim_inferior_intervalo, lim_superior_intervalo))
                lim_inferior_intervalo = lim_superior_intervalo
                break
            else:
                if lim_superior_intervalo <= fin_rango_origen:
                    # CASO 5
                    intervalos_resultantes.append((lim_inferior_intervalo, inicio_rango_origen))
                    intervalos_resultantes.append((inicio_rango_destino, inicio_rango_destino + (lim_superior_intervalo - inicio_rango_origen)))
                    lim_inferior_intervalo = lim_superior_intervalo
                    break
                else:
                    # CASO 6
                    intervalos_resultantes.append((lim_inferior_intervalo, inicio_rango_origen))
                    intervalos_resultantes.append((inicio_rango_destino, inicio_rango_destino + longitud_rango))
                    lim_inferior_intervalo = fin_rango_origen
        else:
            if lim_inferior_intervalo < fin_rango_origen:
                if lim_superior_intervalo <= fin_rango_origen:
                    # CASO 2
                    imagen_lim_inferior = aplicar_rango_a_numero(lim_inferior_intervalo, rango)
                    image_lim_superior = aplicar_rango_a_numero(lim_superior_intervalo, rango)
                    intervalos_resultantes.append((imagen_lim_inferior, image_lim_superior))
                    lim_inferior_intervalo = lim_superior_intervalo
                    break
                else:
                    # CASO 3
                    imagen_lim_inferior = aplicar_rango_a_numero(lim_inferior_intervalo, rango)
                    imagen_fin_rango_origen = aplicar_rango_a_numero(fin_rango_origen, rango)
                    intervalos_resultantes.append((imagen_lim_inferior, imagen_fin_rango_origen))
                    lim_inferior_intervalo = fin_rango_origen
            else:
                # CASO 1
                pass
        
        if lim_inferior_intervalo >= lim_superior_intervalo:
            break
    
    if lim_inferior_intervalo < lim_superior_intervalo:
        intervalos_resultantes.append((lim_inferior_intervalo, lim_superior_intervalo))
        
    return intervalos_resultantes

linea_semilla = input()

semillas = [int(x) for x in re.findall(r"\d+", linea_semilla)]

intervalos_semillas = [(inicio, inicio+longitud) for inicio, longitud in zip(semillas[::2], semillas[1::2])]

input() # Ignorar linea vacía

rangos_semillas_tierra = obtener_rangos_mapa()
rangos_tierra_abono = obtener_rangos_mapa()
rangos_abono_agua = obtener_rangos_mapa()
rangos_agua_luz = obtener_rangos_mapa()
rangos_luz_temperatura = obtener_rangos_mapa()
rangos_temperatura_humedad = obtener_rangos_mapa()
rangos_humedad_localizacion = obtener_rangos_mapa()

intervalos_tierra = []
for intervalo in intervalos_semillas:
    intervalos_tierra += aplicar_rangos_a_intervalo(intervalo, rangos_semillas_tierra)

intervalos_tierra = colapsar_intervalos(intervalos_tierra)

intervalos_abono = []
for intervalo in intervalos_tierra:
    intervalos_abono += aplicar_rangos_a_intervalo(intervalo, rangos_tierra_abono)

intervalos_abono = colapsar_intervalos(intervalos_abono)

intervalos_agua = []
for intervalo in intervalos_abono:
    intervalos_agua += aplicar_rangos_a_intervalo(intervalo, rangos_abono_agua)

intervalos_agua = colapsar_intervalos(intervalos_agua)

intervalos_luz = []
for intervalo in intervalos_agua:
    intervalos_luz += aplicar_rangos_a_intervalo(intervalo, rangos_agua_luz)

intervalos_luz = colapsar_intervalos(intervalos_luz)

intervalos_temperatura = []
for intervalo in intervalos_luz:
    intervalos_temperatura += aplicar_rangos_a_intervalo(intervalo, rangos_luz_temperatura)

intervalos_temperatura = colapsar_intervalos(intervalos_temperatura)

intervalos_humedad = []
for intervalo in intervalos_temperatura:
    intervalos_humedad += aplicar_rangos_a_intervalo(intervalo, rangos_temperatura_humedad)

intervalos_humedad = colapsar_intervalos(intervalos_humedad)

intervalos_localizacion = []
for intervalo in intervalos_humedad:
    intervalos_localizacion += aplicar_rangos_a_intervalo(intervalo, rangos_humedad_localizacion)

intervalos_localizacion = colapsar_intervalos(intervalos_localizacion)

print(sorted(intervalos_localizacion)[0][0])
