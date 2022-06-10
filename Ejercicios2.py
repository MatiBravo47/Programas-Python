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