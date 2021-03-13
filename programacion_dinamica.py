import sys

def fibonacci_recursivo(n): #este codigo es ineficiente
    print(n)
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_dinamico(n, memo={}):
    print(n, memo)
    if n == 0 or n == 1:
        return 1
    
    try: #verifica si puede ser ejecutada, si el dicionario no tiene key entonces ejecuta la recursion.
         #¿hay memo[n]? si no hay, ejecute la recursion   
         # busca un key de una n registrada y lo retorna.     
        return memo[n]
        
    except KeyError:
        
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado
    

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)