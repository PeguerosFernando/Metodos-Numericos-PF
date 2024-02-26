#Funcion, proximamente modificable por el usuario
def f(x):
    return x**2-3
#Tolerencia y limite de iteracions, proximamente modificable
TOL = 1e-4
N = 100
print("Metodo de la secante para la funcion x^2-3")
#Limites recibidos por el usuario:
p0, p1 = [float(x) for x in input("Escriba dos valores iniciales donde evaluar la funcion: ").split()]
f0, f1 = f(p0), f(p1)
n = 1
while n < N:
    p = p1-f1*(p1-p0)/(f1-f0)
    if abs(p-p1) < TOL:
        print("Valor cercano a la raiz encontrada en x={}" .format(p))
        break
    n+=1
    p0 = p1
    f0 = f1
    p1 = p
    f1 = f(p)
if not(n < N):
    print("El metodo fracaso despues de {} iteraciones" .format(n))