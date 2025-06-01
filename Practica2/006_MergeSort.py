# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 16:46:00 2025

@author: k
"""
############# MERGESORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        izquierda = merge_sort(arr[:mid])
        derecha = merge_sort(arr[mid:])
        return merge(izquierda, derecha)
    return arr

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

print("MergeSort:", merge_sort([5, 2, 9, 1, 5, 6]))


