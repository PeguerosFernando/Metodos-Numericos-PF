from .Common.Functions import *

def Secante (f, I, N=100, TOL=1e-8, E="A"):
    """
    Metodo de la Secante

    Args:
        f (array): Funcion a evaluar
        I (list): Intervalo en el cual evaluar nuestra función
        N (int, optional): Numero de iteraciones, por defecto a 100.
        TOL (float, optional): Tolerancia, por defecto a 1e-8.
        E (str, optional): tipo de error a utilizar por defecto "Absoluto".

    Returns:
        Solucion: regresa el valor más cercano a la raiz encontrado
    """
    a, b = I
    fa, fb = Eval(f,a), Eval(f,b)
    n = 1
    while (n < N):
        try:
            t=1/(fb-fa)
        except:
            print("¡Intente un nuevo intervalo!\nSe ha intentado dividr por 0")
        p = b-fb*(b-a)/(fb-fa)
        if (Errores(E)(p,b) < TOL):
            return p
        n+=1
        a = b
        fa = fb
        b = p
        fb = Eval(f,p)
