# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def recur_fibo(n):#Definicion de funcion de fibonacci
   if n <= 1:#Comparicion del numero n sea mayor que 1
       return n# Retorna n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2)) #LLamada recursiva de la funcion

nterms = 21843705 #Numero de expediente para hacer la secuencia

# check if the number of terms is valid
if nterms <= 0:# Comparacion de seguridad
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")#Bucle de impresion
   for i in range(nterms):
       print(recur_fibo(i))