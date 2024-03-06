from Metods import *
import os

f, df, I, p = None, None, None, None,
N, Tol, E = 100, 1e-9, "A"

errors={
    "A": "Abasoluto",
    "R": "Real",
    "RM": "Real Máximo",
    "D": "Distancia"
}

def clear():
    os.system('cls')

def Menu():
    print("Bienvenido al sistema de Metodos Numericos")
    print("Seleccione alguna de las opciones: ")
    print("1.- Modificar parametros")
    print("2.- Utilizar algún metodo")
    print("3.- Salir\n")
    
def Mod():
    print("¿Qué parametro quiere modificar?")
    print("1.- Función")
    print("2.- Derivda de la Función")
    print("3.- Intervalo o Punto inicial")
    print("4.- Numero de iteraciones")
    print("5.- Tolerancia")
    print("6.- Tipo de error")
    print("7.- Regresar")

def Display():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Funcion F: ", f)
    if (df):
        print("Derivada de F: ", df)
    if (p):
        print("Punto inicial: ", p)
    else:
        print("Intervalo: ", I)
    print("Numero de iteraciones: ", N)
    print("Tolerencia: ", Tol)
    print("Tipo de error: ", errors[E])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def Metod():
    print("Seleccione el metodo que desea usar")
    print("1.- Biseccion")
    print("2.- Newton")
    print("3.- Punto fijo")
    print("4.- Secante")
    print("5.- Regresar")

while (True):
    clear()
    Display()
    Menu()
    key=input("")
    if(key=="1"):
        while (True):
            clear()
            Display()
            Mod()
            key=input("")
            if(key=="1"):
                clear()
                Display()
                f=Funcion()
            if(key=="2"):
                clear()
                Display()
                df=Funcion()
            if(key=="3"):
                while (True):
                    clear()
                    Display()
                    print("1.- Intervalo\n2.- Punto")
                    key=input("")
                    if(key=="1"):
                        I=Intervalo()
                        p=None
                        break
                    elif(key=="2"):
                        p=int(input("")) #Falta un check in
                        I=None
                        break
            if(key=="4"):
                clear()
                Display()
                N=int(input("")) #Falta un check in
            if(key=="5"):
                clear()
                Display()
                TOL=float(input("")) #Falta un check in
            if(key=="6"):
                clear()
                Display()
                print("Selecciona el tipo de errror")
                print("A.- Absoluto")
                print("R.- Real")
                print("RM.- Real Maximo")
                print("D.- Distancia")
                typ=input("")
                while (typ not in errors):
                    clear()
                    Display()
                    print("Selecciona el tipo de errror")
                    print("A.- Absoluto")
                    print("R.- Real")
                    print("RM.- Real Maximo")
                    print("D.- Distancia")
                    typ=input("")
                E=typ
            if(key=="7"):
                break
    elif(key=="2"):
        while(True):
            clear()
            Display()
            Metod()
            key=input("")
            if(key=="1"):
                clear()
                Display()
                if (f and I):
                    print("Solucion/es encontradas: ", Biseccion(f, I, N, Tol, 20 , E)) #Falta caso no hay soluciones
                    input("Presiona para continuar...")
                else:
                    print("¡Hacen falta parametros!")
                    input("Presiona para continuar...")
            elif(key=="2"):
                clear()
                Display()
                if (f and df and I):
                    print("Solucion/es encontradas: ", NewtonI(f, df, I, N, Tol, 20, E)) #Falta caso no hay soluciones
                    input("Presiona para continuar...")
                elif (f and df and p):
                    print("Solucion/es encontradas: ", NewtonP(f, df, p, N, Tol, E)) #Falta caso no hay soluciones
                    input("Presiona para continuar...")
                else:
                    print("¡Hacen falta parametros!")
                    input("Presiona para continuar...")
            elif(key=="3"):
                clear()
                Display()
                if (f and p):
                    print("Punto fijo encontrado en: ", PuntoFijo(f, p, N, Tol, E)) #Falta caso no hay soluciones
                    input("Presiona para continuar...")
                else:
                    print("¡Hacen falta parametros!")
                    input("Presiona para continuar...")
            elif(key=="4"):
                clear()
                Display()
                if (f and I):
                    print("Solucion encontrada: ", Secante(f, I, N, Tol, )) #Falta caso no hay soluciones
                    input("Presiona para continuar...")
                else:
                    print("¡Hacen falta parametros!")
                    input("Presiona para continuar...")
            elif(key=="5"):
                break
    elif(key=="3"):
        print("¡Hasta pronto!")
        break