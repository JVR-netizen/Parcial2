import math

CAPACIDAD_CAMION = 29  
PRECIO_CAMION = 150000

while True:
    print("\n--- COTIZACIÓN DE TRANSPORTE ---")

    
    while True:
        nombre = input("Ingrese nombre del cliente: ")
        if len(nombre) >= 3:
            break
        else:
            print("Error: El nombre debe tener al menos 3 letras")

    
    while True:
        telefono = input("Ingrese teléfono (8 a 9 dígitos): ")
        if telefono.isdigit() and 8 <= len(telefono) <= 9:
            break
        else:
            print("Error: Teléfono inválido")

    
    while True:
        try:
            largo = float(input("Ingrese largo de la caja en cm: "))
            ancho = float(input("Ingrese ancho de la caja en cm: "))
            alto = float(input("Ingrese alto de la caja en cm: "))

            if largo > 0 and ancho > 0 and alto > 0:
                break
            else:
                print("Error: Las dimensiones deben ser mayores a 0")
        except:
            print("Error: Debe ingresar números")

    
    while True:
        try:
            cantidad_cajas = int(input("Ingrese cantidad de cajas: "))
            if cantidad_cajas > 0:
                break
            else:
                print("Error: Debe ser mayor a 0")
        except:
            print("Error: Debe ingresar un número entero")

    
    largo_m = largo / 100
    ancho_m = ancho / 100
    alto_m = alto / 100

    volumen_caja = largo_m * ancho_m * alto_m

    cajas_por_camion = CAPACIDAD_CAMION / volumen_caja

    camiones = math.ceil(cantidad_cajas / cajas_por_camion)

    total = camiones * PRECIO_CAMION

    
    print("\n--- RESULTADO ---")
    print("Cliente:", nombre)
    print("Teléfono:", telefono)
    print("Cantidad de cajas:", cantidad_cajas)
    print("Camiones necesarios:", camiones)
    print("Valor total: $", total)

    
    opcion = input("\n¿Desea hacer otra cotización? (s/n): ").lower()
    if opcion != "s":
        print("Programa finalizado")
        break

