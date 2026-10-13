''' 
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes. 
''' 
# PROBLEMA 
# calcular el importe del recibo a partir del consumo del mes

# ENTRADAS
# consumo : float, kWh, >= 0
# costo_hora : float, $, >= 0

# SALIDAS
# importe_recibo : float, $, >= 0

# REGLAS Y SUPUESTOS
# - Valores fijos del problema (tarifas, porcentajes, topes).
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
 
# ALGORITMO 
# 1. Leer consumo
# 2. Si consumo <= 150: 
#       importe_recibo = consumo * 1.00
# 3. En caso contrario, si consumo <= 280:
#       importe_recibo = consumo * 1.50
# 4. En caso contrario:
#       importe_recibo = consumo * 3.00
# 5. Mostrar importe_recibo
 
# CASOS DE PRUEBA 
# caso1: consumo = 100, importe_recibo = 100.00
# caso2: consumo = 150, importe_recibo = 300.00
# caso3: consumo = 200, importe_recibo = 300.00
# caso4: consumo = 280, importe_recibo = 420.00
# caso5: consumo = 300, importe_recibo = 900.00

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES
# leer_consumo() -> consumo : lee el consumo del mes en kWh.
# calcular_importe(consumo, costo_por_kWh) -> importe_recibo : calcula el importe del recibo a partir del consumo y el costo por kWh.
# mostrar_importe(importe_recibo) -> None : muestra el importe del recibo.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leer_consumo():
    consumo = float(input("Ingrese el consumo del mes en kWh: "))
    return consumo

def calcular_importe(consumo):
    if consumo <= 150:
        importe_recibo = consumo * 1.00
    elif consumo <= 280:
        importe_recibo = consumo * 1.50
    else:
        importe_recibo = consumo * 3.00
    return importe_recibo

def mostrar_importe(importe_recibo):
    print(f"El importe del recibo es: ${importe_recibo:.2f}")

