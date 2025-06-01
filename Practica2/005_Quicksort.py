# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 16:38:18 2025

@author: k
"""
####################QUICKSORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0] #Pivote
    left = [x for x in arr[1:] if x <= pivot] #Menores o iguales al pivote
    right = [x for x in arr[1:] if x > pivot] #Mayores al pivote
    return quick_sort(left) + [pivot] + quick_sort(right)

print("QuickSort:", quick_sort([5, 2, 9, 1, 5, 6]))


