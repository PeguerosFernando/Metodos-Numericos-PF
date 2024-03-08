from .Common.Functions import *
from .Biseccion import Biseccion

def NewtonP (f, df, a, N=100, TOL=1e-8, E="A"):
    """
    Metodo de Newton dado un punto

    Argumentos:
        f (array): Funcion a evaluar dada por el usuario
        df (array): Derivada de la funcion dada por el usuario, se puede evitar esto usando una aproximación númerica de la derivada
        a (float): Punto inicial dado por el usuario
        N (int, optional): Numero de iteraciones, por defecto 100.
        TOL (float, optional): Tolerancia, por defecto 1e-8.
        E (str, optional): Error utilizado, por defecto "Absoluto".

    Salida:
        solución: solución encontrada
    """
    a=float(a)
    n = 0
    while (n < N):
        try:
            t=1/(Eval(df,a))
        except:
            print("¡Introduzca otra semilla!\nSe ha intentado dividir por 0")
            break
        else:
            continue
        b = a-((Eval(f,a))/(Eval(df,a)))

        if (Errores(E)(b,a)) < TOL:
            return b
        n+=1
        a = b

def NewtonI (f, df, I, N=100 , TOL=1e-8, N_S=20, E="A"):
    """
    Version de Newton dado un intervalo

    Argumentos:
        f (array): Funcion a evaluar dada por el usuario
        df (array): Derivada de la funcion dada por el usuario, se puede evitar esto usando una aproximación númerica de la derivada
        a (float): Punto inicial dado por el usuario
        N (int, optional): Numero de iteraciones, por defecto a 100.
        TOL (float, optional): Tolerancia, por defecto a 1e-8.
        N_S (int, optional): Numrero de subintervalos, por defecto a 20.
        E (str, optional): tipo de error a utilizar por defecto "Absoluto".

    Salida:
        solucuión: solución encontrada
    """
    Sol=Biseccion(f, I, 10, TOL, N_S, E, True) #Refinamos con el metodo de la bisección
    AllSol=[]
    for a in Sol:
        n=0
        while (n < N):
            try:
                t=1/(Eval(df,a))
            except:
                print("¡Introduzca otra semilla!\nSe ha intentado dividir por 0")
                break
            else:
                continue
            b = a-(Eval(f,a)/Eval(df,a))
            if (Errores(E)(b,a)) < TOL:
                AllSol.append(b)
                break
            n+=1
            a = b
    return AllSol
