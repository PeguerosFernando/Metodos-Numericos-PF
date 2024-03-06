from .Common.Functions import *

def Biseccion(f, I, N=100, TOL=1e-8, N_S=20, E="A", Ignore=False):
    """
    Metodo de la Biseccion

    Argumentos:
        f (array): Funcion a ser evaluada
        I (list): Intervalo dado por el usuario
        N (int, optional): Numero de iteraciones, por defecto a 100.
        TOL (float, optional): Tolerancia, por defecto a 1e-8.
        N_S (int, optional): Numrero de subintervalos, por defecto a 20.
        E (str, optional): tipo de error a utilizar por defecto "Absoluto".
        Ignore (boolean, optional): En caso de querer hacerlo en menos iteraciones usar verdadero para ignorar la tolerancia

    Salida:
        Soluciones: Lista con las soluciones encontradas en el intervalo dado para la funcion
    """
    
    S_ = SubIntervalo(I, N_S+1)
    S_s = Signo(f, S_)
    P_Sol = PosSoluciones(S_, S_s)
    Sol=[]
    if (not(len(P_Sol))):
        print("¡No se ha encontrado ninguna solución para el intervalo y la función dadas!")
    else:
        for a, b in P_Sol:
            n = 0
            while (n < N):
                p = (a+b)/2
                if (Errores(E)(a,p)<=TOL):
                    Sol.append(p)
                    break
                n+=1
                if (Signo_(f,a)*Signo_(f,p) > 0):
                    a = p
                else:
                    b = p
            if(Ignore):
                Sol.append(p)
    return Sol