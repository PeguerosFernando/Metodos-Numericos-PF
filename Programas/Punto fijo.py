#Funcion, proximamente modificable por el usuario
def f(x):
    e = 2.71828
    return e**(-x)
#Tolerencia y limite de iteracions, proximamente modificable
TOL = 1e-4
N = 100
print("Metodo del punto fijo para la funcion e^(-x)")
#Valor inicial ingresado por el usuraio:
p0 = float(input("Escriba un valor inicial: "))
#Iniciamos el ciclo del algoritmo, en un futuro sera una funcion
n = 0
while n < N:
    p = f(p0)
    if abs(p-p0) < TOL:
        print("Valor mas cercano al punto fijo encontrado en x={}" .format(p))
        break
    n+=1
    p0 = p
if not(n < N):
    print("El metodo fracaso despues de {} iteraciones" .format(n))