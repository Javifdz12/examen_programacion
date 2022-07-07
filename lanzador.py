
import random
from cuenta import cuenta_bancaria
def main():
    #Ejercicio1:
    x=random.randint(10,20)
    y=random.randint(1,200)
    print(f'Ya veo quiere que quiere: {x} manzanas y {y} caramelos')
    s=x+y
    z=(x*3.50)+(y*0.5)
    if s<20:
        print(f'Son {z} euros')
    else:
        z=(x*3.50)+(y*0.5)-0.70
        s=s-20
        while s>20:
            s=s-20
            z=z-0.70
        else:
            print(f'Son {z} euros')

    #Ejercicio2
    while r!=3:
        r=int(input(f'¿Desea realizar alguna operacion?:\n 1- Ingresar.\n 2- Retirar.\n 3- Salir'))
        cuenta1=cuenta_bancaria("javi",1000)
        if r==1:
            n=float(input('¿Que cantidad deseas ingresar?:\n'))
            cuenta1.ingresar(n)
            cuenta1.operaciones.append(n)
            cuenta1.imprimir()
        elif r==2:
            m=float(input('¿Que cantidad deseas retirar?:\n'))
            cuenta1.retirar(m)
            cuenta1.operaciones.append(-m)
            cuenta1.imprimir()
        else:
            print('Opcion incorrecta')
    else:
        cuenta1.imprimir
        print(cuenta1.operaciones)


