''' 
Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o fracción. 
El cobro máximo es de $150. El sistema recibe el tiempo de estancia en minutos y 
muestra el importe a cobrar. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración. 
# Se calcula el importe a cobrar por el tiempo de estancia en el estacionamiento.

# ENTRADAS 
# tiempo_estancia : float, minutos, >= 0
 
# SALIDAS 
# importe : float, $, >= 0

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer tiempo_estancia
# 2. Si tiempo_estancia <= 60:
#       importe = 20
# 3. En caso contrario:
#       horas_adicionales = (tiempo_estancia - 60) / 60
#       importe = 20 + horas_adicionales * 15
#       Si importe > 150:
#           importe = 150
# 4. Mostrar importe

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# caso1: 45 -> 20
# caso2: 60 -> 20 + 15 = 35
# caso3: 61 -> 20 + 15 * 1.5 = 52.5
# caso4: 150 -> 20 + 15 * 2 = 65
# caso5: 600 -> 150

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leer_minutos() -> tiempo_estancia : lee el tiempo de estancia en minutos.
# calcular_cobro(tiempo_estancia) -> importe : calcula el importe a cobrar según
# mostrar_cobro(importe) -> None : muestra el importe a cobrar.
 
# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def leer_minutos():
    tiempo_estancia = float(input("Ingrese el tiempo de estancia en minutos: "))
    return tiempo_estancia

def calcular_cobro(tiempo_estancia):
    if tiempo_estancia <= 60:
        return 20
    else:
        horas_adicionales = (tiempo_estancia - 60) / 60
        importe = 20 + horas_adicionales * 15
        if importe > 150:
            importe = 150
        return importe

def mostrar_cobro(importe):
    print(f"Importe a cobrar: ${importe:.2f}")
