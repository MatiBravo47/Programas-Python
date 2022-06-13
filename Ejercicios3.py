#Ejercicio1
class Persona: 
    #nombre, edad, dni
    #constructores
    def __init__(self):
        self.nombre=""
        self.edad=0
        self.dni=0
    """
        def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    """
    def __str__(self):
        return f"Nombre:{self.nombre} - edad: {self.edad} - DNI{self.dni} "
    
    def set_nombre(self , nombre ):
        self.nombre=nombre
    
    def set_edad(self,edad):
        self.edad=edad 

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def Imprimir_persona (self):
        return f"Nombre:{self.nombre} - edad: {self.edad} - DNI{self.dni} "
    
#Programa principal 
#p=Persona("Marcela Cerda",25,1111111)
p1=Persona()
#print(p.Imprimir_persona())
#print(p)
nombre=input("Ingrese nombre: ")
edad=int(input("Ingrese edad: "))
dni=int(input("Ingrese dni"))
#p1.nombre=nombre

p1.set_nombre(nombre)
p1.set_edad(edad)
p1.dni=dni
print(p1)
