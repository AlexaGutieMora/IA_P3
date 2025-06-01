# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 15:45:56 2025

@author: k
"""
################# INTERCAMBIO
def intercambio(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] ###
    return arr
print("Intercambio :", bubble_sort([5, 2, 9, 1, 5, 6]))
