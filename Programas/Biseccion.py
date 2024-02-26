#Funcion, proximamente modificable por el usuario
def f(x):
    return 2*x-3
#Tolerencia y limite de iteracions, proximamente modificable
TOL = 1e-4
N = 100
print("Metodo de la biseccion para la funcion 2x-3")
#Limites recibidos por el usuario:
a, b = [float(x) for x in input("Escriba los exteremos donde evaluar la funcion: ").split()]
#Por el momento se comprueba que los extremos son adecuados, en el futuro se analizaran sub intervalos
while f(a)*f(b)>0:
    print("Los extremos no son apropiados por favor intrduzca dos extremos adecuados: ")
    a, b = [float(x) for x in input("Escriba los exteremos donde evaluar la funcion: ").split()]
#Iniciamos el ciclo del algoritmo, en un futuro sera una funcion
n = 0
while n < N:
    p = (a+b)/2
    if (b-a)/2 < TOL:
        print("Valor más cercano a la raiz encontrado en x={}" .format(p))
        break
    n+=1
    if f(a)*f(p) > 0:
        a = p
    else:
        b = p
if not(n < N):
    print("El metodo fracaso despues de {} iteraciones" .format(n))