import random
#valor de cada btc en dolares
d=random.randint(5000,50000)
def DollarToEuros(num_btc):
    euros=(num_btc*d)/1.14
    print(f'Tienes {num_btc} btcs que equivalen a {euros} euros')
    return euros

def btc_a_euros():
    valor=d/1.14
    return valor
def peligro():
    if btc_a_euros()<10000:
        print("¡¡¡¡¡¡Peligrooo!!!!! BTC esta por debajo de 10000")
    else:
        print(f'De momento no hay peligro, BTC tiene ahora mismo un valor de {btc_a_euros()}')
def staking(capital,interes_anual,años):
    ingreso_anual=(capital*interes_anual)/100
    print(f'Cada año vas a generar {ingreso_anual} euros, por tanto en {años} años habras generado {ingreso_anual*años} euros, por lo que terminaras con {(ingreso_anual*años)+capital} euros de capital')


staking(DollarToEuros(4),5,5)