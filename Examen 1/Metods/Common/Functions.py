import numpy as np
import matplotlib.pyplot as plt

def Errores (tipo='A'): #Esta función la tome del codigo ejemplo en el GitHub
    """
    Llama y evalua el error según el tipo

    Argumentos:
        tipo (str): Según el error que se desee evaluar y sea más comodo para el usuario, por defecto se llama al error Absoluto

    Salida:
        Err[tipo]: Regresara la función para calcular el error
    """
    Err = {'A': lambda pn1, pn: abs(pn1-pn), 
            'R': lambda pn1, pn: abs(pn1-pn)/abs(pn),
            'RM': lambda pn1, pn: abs(pn1-pn)/abs(max([pn, pn1])),
            'D': lambda a, b: (b-a)/2}
    return Err[tipo]

def Funcion(): #Mi función para que el usuario agregue su función, revisando que sea correcta de manera recursiva
    """
    Solicita al usuario su función en notación de codigo
    
    Salida:
        f: La entrada del usuario en formato string
    """
    F = input("Introduzca su funcion de x, (Pude utilizar np para usar funcion de numpy):\n")
    try:
        x = 0 #Esto podría fallar para funciones no definidas en 0, se necesita mejorar
        f = eval(F)
    except:
        print("¡Introduzca correctamente la función!")
        F = Funcion()
        return F
    else:
        return F

def Eval(f, x):
    """
    Funcion para evaluar puntualmente la función

    Argumentos:
        f (array): Función a evaluar
        x (float): Punto en el que evaluar f

    Salida:
        f(x): Valor de la función en x
    """
    F = float(eval(f))
    return F

def Intervalo(): #Función para recibir el intervalo del usuario corrovorando que sea un intevalo valido
    """
    Solicita al usuario un intervalo valido

    Salida:
        [a,b]: Una lista con el par ordenado de menor a mayor
    """
    x = list(map(float, input("Ingrese dos valores para su intervalo: ").split()))
    if not(len(x) == 2):
        print("¡Introduzca dos valores para el intervalo por favor!")
        I = Intervalo()
        return I
    else: #Me gustaría mejorar estos if y else
        a, b = x
        if a == b:
            print("¡Introdusca un intervalo valido con dos valores diferentes!")
            I = Intervalo()
            return I
        elif (a < b):
            return x
        else:
            x = [b,a]
            return x

def SubIntervalo(I, N=20): #Funcion para dividir el intervalo
    """
    Divide en subintervalos un intervalo dado

    Argumentos:
        I (list): Es el intervalo que se desea subdividir
        N (int, optional): Es el numero de subintervalos-1 que se desean, por defecto son 20

    Salida:
        [a, ..., b]: Regresa una lista con los puntos de nuestros subintervalos equidistantes
    """
    a, b = I
    x = list(np.linspace(a, b, N)) #Me gustaría implementarlo despues para arrays de numpy
    return x

def Signo (f, I):
    """
    Regresa una lista con los signos

    Argumentos:
        f (array): La función a ser evaluada
        I (list): El intervalo en el que se evaluara el signo

    Salida:
        list: Lista con los signos de los intervalos
    """
    #En esta parte podría ser más fácil utilizar arrays pero no pude hacer funcionar mi funcion para un array
    s=[] 
    for x in I:
        if (eval(f) > 0):
            s.append(1)
        elif (eval(f) < 0):
            s.append(-1)
        else:
            s.append(0)
    return s

def Signo_ (f, x):
    """
    Version para un unico valor de la funcion Signo

    Argumentos:
        f (array): Funcion a evaluar
        x (float): Punto donde evaluar

    Salida:
        Signo: Signo de la funcion en x
    """
    if (eval(f) > 0):
        return 1
    elif (eval(f) < 0):
        return -1
    else:
        return 0

def PosSoluciones (I, S):
    """
    Regresa una lista de duplas con los extremos de posibles soluciones

    Argumentos:
        I (list): Lista del intervalo o subintervalos
        S (list): Lista del signo asociado al intervalo o subintervalos

    Salida:
        list: Lista con las duplas donde se encontraron cambios de signo
    """
    PS=[]
    a = I[0]
    s = S[0]
    for i,j in zip(I, S):
        if (s*j > 0):
            a=i
            s=j
        else:
            if(s*j == 0):
                pass
            else:
                PS.append([a,i])
                a=i
                s=j
    return PS
