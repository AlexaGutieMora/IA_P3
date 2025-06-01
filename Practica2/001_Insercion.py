# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 15:10:42 2025

@author: k
"""

######################## INSERCIÓN DIRECTA 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  #Elemento a insertar
        j = i - 1
        #Mueve los elementos mayores a la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        #Inserta el elemento en su lugar
        arr[j + 1] = key
    return arr

print("Inserción directa:", insertion_sort([5, 2, 9, 1, 5, 6]))
