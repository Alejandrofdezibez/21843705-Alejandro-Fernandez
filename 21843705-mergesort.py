import random
import time
import multiprocessing as mp
import math
def seq_mergesort(array, *args): #Definicion de mergesort en secuencial aplicamos el enfoque de divide y venceras para solucinar este apartado
    # Use a breakpoint in the code line below to debug your script.
    if not args:
        seq_mergesort(array,0, len(array)-1)
        return array
    else:
        left, right = args
        if left < right:
            mid =(left + right) // 2 #Dividimos el array en 2 para cada vez ir obteniendo fragmentos mas pequeños del array
            seq_mergesort(array,left,mid)#En este parte tratamos la primera parte del de la division del array que va desde el inicio 0 hasta la mitad
            seq_mergesort(array,mid+1, right)#En esta parte tratamos el array desde la mitad mas una posicion hasta el final del array
            merge(array, left, mid, right)# Seguidamente procedemos a rejuntar las partes ordenadas

def merge(array, left, mid, right): #Definicion de la funcion encargada de ordenar el array
    left_temp_arr = array[left:mid+1].copy()
    right_temp_arr = array[mid+1:right+1].copy()

    left_temp_index = 0
    right_temp_index = 0
    merge_index = left
#Bucle de comparacion de elementos en el que dependiendo de los elementos iran variando sus posiciones dentro del array para que nos devuelva sus elementos
while left_temp_index < (mid-left +1) or right_temp_index < (right - mid):
    if left_temp_index < (mid-left+1) and right_temp_index < (right-mid):
        if left_temp_arr[left_temp_index] <= right_temp_arr[right_temp_index]:
            array[merge_index] = left_temp_arr[left_temp_index]
            left_temp_index +=1
        else:
            array[merge_index] = right_temp_index[right_temp_index]
            right_temp_index +=1
        elif left_temp_index < (mid-left + 1):
            array[merge_index] = left_temp_arr[left_temp_index]
            left_temp_index += 1
        elif right_temp_index < (right - mid):
                array[merge_index] = right_temp_arr[right_temp_index]
                right_temp_index += 1
                merge_index += 1

def par_mergesort(array, *args):#Definicion de la funcion de paralelizar el mergesort
    if not args: #first call
        shared_array = mp.RawArray('i', array) # Creacion de una array bruto para el almacenamiento de los elementos
        par_mergesort(shared_array, 0, len(array)-1, 0)
        array[:] = shared_array
        return array
    else:
        left, right, depth = args
        if (depth >= math.log(mp.cpu_count(), 2)):
            seq_mergesort(array, left, right)
        elif (left < right):
            #Inicio del enfoque de divide y venceras, en esta parte del codigo encar procedomos a asignar el trabajo a los cores
            mid = (left + right) // 2
            left_proc = mp.process(target = par_mergesort, args =(array,left,mid,depth +1))
            left_proc.start()
            par_mergesort(array, mid+1, right, depth+1)
            left.proc.join()
            merge(array, left, mid, right)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    NUM_EVAL_RUNS = 1
    print('Creando Array...')
    array = [random.randint(0,10_000) for i in range(21_843_705)]

    print('Evaluando a mano ...')
    sequential_result = seq_mergesort(array.copy())
    sequential_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_mergesort(array.copy())
        sequential_time += time.perf_counter() - start
        sequential_time /= NUM_EVAL_RUNS

    print('Evaluando Paralelo...')
    parallel_result = par_mergesort(array.copy())
    parallel_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_mergesort(array.copy())
        parallel_time += time.perf_counter() - start
        parallel_time /=NUM_EVAL_RUNS

        if sequential_result != parallel_result:
            raise Exception('Mal')
        print('Seq Time: {:.2f} ms'.format(sequential_time*1000))
        print('Par Time: {:.2f} ms'.format(parallel_time * 1000))
        print('Incre: {:.2f} ms'.format(sequential_time/parallel_time))
        print('Ef: {:.2f}%'.format(100*(sequential_time/parallel_time)/mp.cpu_count()))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
