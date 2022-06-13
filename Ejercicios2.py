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