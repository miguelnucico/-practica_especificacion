''' 
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de 
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket con 
subtotal, descuento, IVA y total.  
''' 
# PROBLEMA 
# Qué se calcula, en una oración. 
# Se calcula el ticket de compra con subtotal, descuento, IVA y total.

# ENTRADAS 
# compra : float, $, >= 0

# SALIDAS 
# subtotal : float, $, >= 0
# descuento : float, $, >= 0
# iva : float, $, >= 0
# total : float, $, >= 0

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer compra
# 2. Si compra >= 5000: 
#       descuento = compra * 0.2
# 3. En caso contrario, si compra >= 1000:
#       descuento = compra * 0.1
# 4. En caso contrario:
#       descuento = 0
# 5. subtotal = compra - descuento
# 6. iva = subtotal * 0.16
# 7. total = subtotal + iva
# 8. Mostrar subtotal, descuento, iva, total

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# caso1: 500 -> 500, 50.0, 72.0, 522.0
# caso2: 900 -> 900, 90.0, 129.6, 939.6
# caso3: 1000 -> 1000, 100.0, 144.0, 1044.0
# caso4: 5000 -> 4000, 1000.0, 640.0, 4640.0

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leer_subtotal() -> compra : lee el monto de la compra.
# calcular_descuento(compra) -> descuento : calcula el descuento a aplicar según el monto
# calcular_IVA(subtotal) -> iva : calcula el IVA a partir del subtotal.
# calcular_total(subtotal, iva) -> total : calcula el total a pagar sumando subtotal e IVA.
# mostrar_ticket(subtotal, descuento, iva, total) -> None : muestra el ticket con 
 
# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def leer_subtotal():
    compra = float(input("Ingrese el monto de la compra: "))
    return compra

def calcular_descuento(compra):
    if compra >= 5000:
        return compra * 0.2
    elif compra >= 1000:
        return compra * 0.1
    return 0

def calcular_IVA(subtotal):
    return subtotal * 0.16

def calcular_total(subtotal, iva):
    return subtotal + iva

def mostrar_ticket(subtotal, descuento, iva, total):
    print("----- TICKET -----")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")
    print("------------------")