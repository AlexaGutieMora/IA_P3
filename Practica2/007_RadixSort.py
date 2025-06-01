# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 16:57:02 2025

@author: k
"""
################# RADIXSORT
def counting_sort_digito(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10
    for i in arr:
        indice = (i // exp) % 10
        conteo[indice] += 1
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1
        i -= 1
    for i in range(n):
        arr[i] = salida[i]
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_digito(arr, exp)
        exp *= 10
    return arr
print("RadixSort:", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))


