from .Common.Functions import *

def PuntoFijo (f, a, N=100, TOL=1e-8, E="A"):
    """
    Metodo para encontrar el punto fijo de una función dada

    Args:
        f (array): Función a la cual se busca un punto fijo
        a (float): Punto inicial para encontrar el punto fijo
        N (int, optional): Numero de iteraciones, por defecto 100.
        TOL (float, optional): Tolerancia, por defecto 1e-8.
        E (str, optional): Error utilizado, por defecto "Absoluto".

    Returns:
        Punto_fijo: Punto donde f(x)=x
    """
    a=float(a)
    n=0
    while (n < N):
        b = Eval(f,a)
        if (Errores(E)(a,b) < TOL):
            return b
        n+=1
        a = b