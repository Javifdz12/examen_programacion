
from cuenta import cuenta_bancaria

r=int(input(f'¿Desea realizar alguna operacion?:\n 1- Ingresar.\n 2- Retirar.\n 3- Salir\n'))
cuenta1=cuenta_bancaria("javi",10000)
while r!=3:
    if r==1:
        n=float(input('¿Que cantidad deseas ingresar?:\n'))
        cuenta1.ingresar(n)
        cuenta1.operaciones.append(n)
        cuenta1.imprimir()
        r=int(input(f'¿Desea realizar alguna operacion?:\n 1- Ingresar.\n 2- Retirar.\n 3- Salir\n'))
    elif r==2:
        m=float(input('¿Que cantidad deseas retirar?:\n'))
        cuenta1.retirar(m)
        cuenta1.operaciones.append(-m)
        cuenta1.imprimir()
        r=int(input(f'¿Desea realizar alguna operacion?:\n 1- Ingresar.\n 2- Retirar.\n 3- Salir\n'))
    else:
        print('Opcion incorrecta')
        r=int(input(f'¿Desea realizar alguna operacion?:\n 1- Ingresar.\n 2- Retirar.\n 3- Salir\n'))
else:
    cuenta1.imprimir
    cuenta1.div_operaciones()