usuario_correcto = "admin"
clave_correcta = "1234"

print("Hola, Bienvenido a Duoc") 

usuario = input("Ingresa tu usuario: ")
clave = input("Ingresa tu clave: ")

if usuario == usuario_correcto and clave == clave_correcta:
    print("Bienvenido, acceso permitido")
else:
    print("Usuario o clave incorrectos")