#1)
def mayor_de_3(n1,n2,n3):
    mayor=0
    if n1>n2 and n1>n3: 
        mayor=n1
    elif n2>n3 and n2>n1:
        mayor=n2
    elif n3>n2 and n3>n1:
        mayor=n3
    else:
        mayor=-1

    return mayor

#Programa principal 
print(f'El mayor es: {mayor_de_3(3,4,1)}')



#3)
precio=int(input("Ingrese el total: "))
pago=int(input("Ingrese el pago del cliente : "))
while pago<precio:
    print("pago insuficiente")
    print(f"falta {precio-pago}")
    pago=int(input("Ingrese el pago del cliente :")) 
vuelto=pago-precio

billetes=[500,100,50,20,10,5,1]
cambio=[0,0,0,0,0,0,0]

vuelto=pago-precio
for i in range(0,len(billetes)): #b es elemento de billetes
    cambio[i]=vuelto//billetes[i]
    vuelto=vuelto-cambio[i]*billetes[i]
print (billetes)
print (cambio)
for i in range(len(cambio)):
    if cambio [i]>0:
        print(cambio[i],billetes[i])
#5)Crear una funcion lambda que devuelva el cuadrado de un valor
# recibido como parametro.Desarrollar ademas un programa para
# verificar el comportamiento de la funcion 
cuadrado = lambda x: x**2
n=int(input("Ingrese un numero"))
print(cuadrado(n))
#6)Crear una funcion lambda para comprobar si un numero es 
# par o impar.Desarrollar ademas un programa para verificar
# el comportamiento de la funcion.
       
#7)

n=int(input("Ingrese un numero entero >a 10:"))
while n<10:
    n=int(input("Error_Ingrese un numero entero >a 10:"))
l=[]
for i in range (1,n+1):
    l.append(i**2) 
print(l)
for i in range(n-10,n,1):
    print(l[i],end=" , ")
#8)Eliminar de una lista de palabras que se encuentren en una 
#segunda lista.Imprimir la lista original de palabras a 
#eliminar y la lista resultante 
