from ejercicios.ejercicio1_luz import leer_consumo, calcular_importe, mostrar_importe
from ejercicios.ejercicio2_calificacion import leer_parciales, calcular_calificacion_final, determinar_estado, mostrar_resultado
from ejercicios.ejercicio3_compra import leer_subtotal, calcular_descuento, calcular_IVA, calcular_total, mostrar_ticket
from ejercicios.ejercicio4_estacionamiento import leer_minutos, calcular_cobro, mostrar_cobro

def menu_principal():
    while True:
        print("Seleccione un ejercicio:")
        print("1. Ejercicio 1: Cálculo de importe de recibo de luz")
        print("2. Ejercicio 2: Cálculo de calificación final y estado del alumno")
        print("3. Ejercicio 3: Cálculo de ticket de compra")
        print("4. Ejercicio 4: Cálculo de cobro por tiempo de estancia en estacionamiento")
        print("5. Salir")

        opcion = input("Ingrese el número del ejercicio que desea ejecutar (1-5): ")

        if opcion == "1":
            consumo=leer_consumo()
            importe_recibo=calcular_importe(consumo)
            mostrar_importe(importe_recibo)
        elif opcion == "2":
            parciales=leer_parciales()
            calificacion_final=calcular_calificacion_final(parciales)
            estado=determinar_estado(calificacion_final)
            mostrar_resultado(calificacion_final, estado)
        elif opcion == "3":
            compra=leer_subtotal()
            subtotal, descuento, iva, total=calcular_total(compra)
            mostrar_ticket(subtotal, descuento, iva, total)
        elif opcion == "4":
            minutos=leer_minutos()
            cobro=calcular_cobro(minutos)
            mostrar_cobro(cobro)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
    