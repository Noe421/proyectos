#practica5

#Noe Ballesteros Garcia 

r=0
n1=0
n2=0

def suma(n1,n2):
    print("Suma de dos numeros")
    print("La suma de " + str(n1) + " + " + str(n2) + " es igual a: ")
    r=n1+n2
    print("" + str(r))

def resta(n1,n2):
    print("la resta de 2 numeros")
    print("la resta de " + str(n1) + " - " + str(n2) + " es igual a: ")
    r=n1-n2
    print("" + str(r))

def multiplicacion(n1,n2):
    print("la multiplicacion de 2 numeros")
    print("la multiplicacion de " + str(n1) + " * " + str(n2) + " es igual a: ")
    r=n1*n2
    print("" + str(r))

def division(n1,n2):
    print("la division de 2 numeros")
    print("la division de " + str(n1) + " / " + str(n2) + " es igual a: ")
    r=n1/n2
    print("" + str(r))

#Arranque
suma(2,2)

resta(6,2)

multiplicacion(4,4)

division(4,12)