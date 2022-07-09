'''Escribir un programa que pregunte el nombre y apellido del usuario. Luego de ser introducidos los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido}, gusto en conocerte!, donde:

{nombre} y {apellido} son los valores introducidos'''
#Declaro variables
nombre=""
apellido=""

#Solicitud de datos
print (">>> Introduce tu nombre:")
nombre = input("> ")
print(">>>Introduce tu apellido:")
apellido = input("> ")

#Mensaje en Pantalla: Metodo .format()
print("Hola {0} {1}, gusto en conocerte!" .format(nombre,apellido))

