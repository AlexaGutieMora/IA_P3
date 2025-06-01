# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 15:42:41 2025

@author: k
"""
###################### SELECCIÓN
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        #Encuentra el mínimo restante
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #Intercambia el mínimo con el primero no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("Seleccion directa:", selection_sort([5, 2, 9, 1, 5, 6]))
