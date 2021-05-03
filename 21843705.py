import os
def Login():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:

    print("1. EjercicioA")
    print("2. EjercicioB")
    print("3. EjercicioC")
    print("4. Salir")

    print("Elige una opcion")

    opcion = Login()

    if opcion == 1:
        os.system('python 21843705-Matrices.py')
    elif opcion == 2:
        os.system('python 21843705-mergesort.py')
    elif opcion == 3:
        os.system('python 21843705-Fibo.py')
    elif opcion == 4:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")
