# LOGIN MAQUINA EXPENDEDORA

usuario_correcto = "javiera"

clave_correcta = "444"



usuario = input("Ingrese su nombre: ")

clave = input("Ingrese su clave: ")



if usuario == usuario_correcto and clave == clave_correcta:

  print("Hola! Bienvenida Javiera")



   

  productos = []

  precios = []

  contador = 0





  def agregar_producto():

    print("\nProductos disponibles:")

    print("1 - Completo $2500")

    print("2 - Bebida $1800")

    print("3 - Papas fritas $2000")



    opcion = int(input("Seleccione un producto (1-3): "))



    if opcion == 1:

      productos.append("Completo")

      precios.append(2500)

    elif opcion == 2:

      productos.append("Bebida")

      precios.append(1800)

    elif opcion == 3:

      productos.append("Papas fritas")

      precios.append(2000)

    else:

      print("Opción inválida")



   

  def calcular_total():

    total = 0

    for precio in precios:

      total = total + precio

    return total



   

  seguir = "si"

  while seguir == "si":

    agregar_producto()

    contador = contador + 1

    seguir = input("¿Desea agregar otro producto? (si/no): ")



  total = calcular_total()



   

  print("\n--- RESUMEN ---")

  print("Usuario:", usuario)

  print("Cantidad de productos:", contador)

  print("Total a pagar:", total)



  if contador > 5:

    print("Gracias por su compra")



else:

    print("Usuario o clave incorrectos")

