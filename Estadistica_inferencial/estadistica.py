import random
import math

def media(x):
    return sum(x) / len(x)

def varianza(x):
    mu = media(x)

    acumulador = 0
    for X in x:
        acumulador += (X - mu)**2

    return acumulador / len(x)

def desviacion_estandar(x):
    return math.sqrt(varianza(x))

if __name__ == '__main__':
    x = [random.randint(1,21) for i in range(20)]
    
    mu = media(x)
    Var = varianza(x)
    sigma = desviacion_estandar(x)
    

    print(f'Arreglo X: {x}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion Estandar = {sigma}')