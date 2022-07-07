import random
def main():
    print('hola')
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

    #Ejercicio5:
    


