print("Intercanvio de clave segura mediante Diffe y Hellman \n")

print("Sistema de generacion de clave de sesion")

nombre=input("\n Ingresa tu nombre: ")

print("\n Seleccion de datos Publicos \n")
p=int(input( nombre +" aqui " +" ingresa un numero primo!: "))
a=int(input( nombre +" ingresa una raiz primitiva del numero primo ingresado: "))

print("\n Seleccion de datos Privados \n")
cprivada=int(input(nombre + " ingresa tu clave privada: "))

cpublica= (a**cprivada)% p
print(nombre + " tu clave publica es: ",cpublica)


yb=int(input("\n "+ nombre + " ingresa la clave publica de la persona con la que quieres comunicarte: "))

print("\n Clave de secion \n")

k = (yb**cprivada)% p
print(nombre+ " la clave de sesion es: ", k)

