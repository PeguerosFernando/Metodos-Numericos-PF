#Funcion y su derivada, proximamente modificable por el usuario
def f(x):
    return x**2-3
def df(x):
    return 2*x
#Tolerencia y limite de iteracions, proximamente modificable
TOL = 1e-4
N = 100
print("Metodo de Newton para la funcion x^2-3")
#Valor inicial ingresado por el usuraio:
p0 = float(input("Escriba un valor inicial: "))
#Iniciamos el ciclo del algoritmo, en un futuro sera una funcion
n = 0
while n < N:
    p = p0-(f(p0)/df(p0)) #Por modificar que la derivada sea distinta de 0
    if abs(p-p0) < TOL:
        print("Valor cercano a la raiz encontrada en x={}" .format(p))
        break
    n+=1
    p0 = p
if not(n < N):
    print("El metodo fracaso despues de {} iteraciones" .format(n))