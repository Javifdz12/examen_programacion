class cuenta_bancaria:

    def __init__(self, titular,fondos):
        if isinstance(titular,str):
            self.titular=titular
        else:
            self.titular="nombre"
        if isinstance(fondos,float):
            self.fondos=fondos
        else:
            self.fondos=0
        self.operaciones=[]


    def imprimir(self):
        print("el cliente",self.titular,"tiene",self.fondos)

    def ingresar(self,x):
        if x<0:
            print("cantidad erronea")
        else:
            self.fondos=x+self.fondos
            print("ahora tienes",self.fondos)

    def retirar(self,y):
        if y>self.fondos:
            print("retirada cancelada")
        elif y<0:
            print("cantidad erronea")
        else:
            self.fondos=self.fondos-y
            print("te quedan",self.fondos)

    def transferir(self,cantidad,cuenta):
        if cantidad>self.fondos:
            print("no es posible hacer la transferencia")
        else:
            cuenta.fondos=cuenta.fondos+cantidad
            self.fondos=self.fondos-cantidad
            print(f'has transferido {cantidad} a {cuenta.titular}')
    def operaciones(self):
        ingresos=[]
        retiros=[]
        for i in self.operaciones:
            if i>=0:
                ingresos.append(i)
            else:
                retiros.append(i)
        return f'Ingresos: {ingresos}\nRetiros: {retiros}'
