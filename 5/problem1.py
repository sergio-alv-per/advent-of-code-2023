import re

def obtener_rangos_mapa():
    rangos = []
    input() # Ignorar título mapa
    rango = input()
    while rango:
        r = tuple(int(x) for x in rango.split(" "))
        rangos.append(r)
        rango = input()
    
    return sorted(rangos)

def encontrar_correspondencia_en_rangos(numero, rangos):
    for rango in rangos:
        inicio_rango_origen = rango[1]
        inicio_rango_destino = rango[0]
        longitud_rango = rango[2]
        if inicio_rango_origen <= numero < inicio_rango_origen+longitud_rango:
            return inicio_rango_destino + (numero - inicio_rango_origen)
    
    return numero

linea_semilla = input()

semillas = [int(x) for x in re.findall(r"\d+", linea_semilla)]

input() # Ignorar linea vacía

rangos_semillas_tierra = obtener_rangos_mapa()
rangos_tierra_abono = obtener_rangos_mapa()
rangos_abono_agua = obtener_rangos_mapa()
rangos_agua_luz = obtener_rangos_mapa()
rangos_luz_temperatura = obtener_rangos_mapa()
rangos_temperatura_humedad = obtener_rangos_mapa()
rangos_humedad_localizacion = obtener_rangos_mapa()


localizacion_minima = 10000000000000000000000000000000
for semilla in semillas:
    correspondencia = encontrar_correspondencia_en_rangos(semilla, rangos_semillas_tierra)
    correspondencia = encontrar_correspondencia_en_rangos(correspondencia, rangos_tierra_abono)
    correspondencia = encontrar_correspondencia_en_rangos(correspondencia, rangos_abono_agua)
    correspondencia = encontrar_correspondencia_en_rangos(correspondencia, rangos_agua_luz)
    correspondencia = encontrar_correspondencia_en_rangos(correspondencia, rangos_luz_temperatura)
    correspondencia = encontrar_correspondencia_en_rangos(correspondencia, rangos_temperatura_humedad)
    correspondencia = encontrar_correspondencia_en_rangos(correspondencia, rangos_humedad_localizacion)

    if correspondencia < localizacion_minima:
        localizacion_minima = correspondencia

print(localizacion_minima)
