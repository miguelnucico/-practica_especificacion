''' 
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración. 
# Se calcula la calificación final de un alumno en una materia a partir de tres parciales. 

# ENTRADAS 
# parcial1 : float, %, [0, 100]
# parcial2 : float, %, [0, 100]
# parcial3 : float, %, [0, 100]

# SALIDAS 
# calificacion_final : float, %, [0, 100]
# aprobado : bool, [True, False]

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
#   Se asumió que si un parcial es menor a 50, el alumno reprueba la materia sin importar los otros parciales.

# ALGORITMO
# 1. Leer parcial1, parcial2, parcial3
# 2. Si parcial1 < 50 o parcial2 < 50 o parcial3 < 50: 
#       aprobado = False
# 3. En caso contrario: 
#       calificacion_final = parcial1 * 0.3 + parcial2 * 0.3 + parcial3 * 0.4
#       aprobado = calificacion_final >= 70
# 4. Mostrar calificacion_final, aprobado

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# caso1: 80, 70, 90 -> 74.0, True
# caso2: 70, 70, 70 -> 74.0, False
# caso3: 100, 100, 40 -> 74.0, False
# caso4: 69, 70, 70 -> 74.0, False

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leer_parciales() -> parcial1, parcial2, parcial3 : lee los tres parciales del alumno.
# calcular_calificacion_final(parcial1, parcial2, parcial3) -> calificacion_final
# determinar_estado(calificacion_final, parcial1, parcial2, parcial3) -> aprobado
# mostrar_resultado(calificacion_final, aprobado) -> None : muestra la calificación final y si el alumno aprobó.
 
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leer_parciales():
    parcial1 = float(input("Ingrese la calificación del primer parcial: "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
    return (parcial1, parcial2, parcial3)

def calcular_calificacion_final(parciales):
    calificacion_final = parciales[0] * 0.3 + parciales[1] * 0.3 + parciales[2] * 0.4
    return calificacion_final

def determinar_estado(calificacion_final, parciales):
    if parciales[0] < 50 or parciales[1] < 50 or parciales[2] < 50:
        return False
    return calificacion_final >= 70

def mostrar_resultado(calificacion_final, aprobado):
    print(f"Calificación final: {calificacion_final:.2f}")
    print("Aprobado" if aprobado else "Reprobado")

