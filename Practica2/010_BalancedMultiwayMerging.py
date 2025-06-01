# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 17:49:36 2025

@author: k
"""
############################ BALANCED MULTIWAY MERGING
def balanced_multiway_merge(arr, k=3):
    if len(arr) <= 1:
        return arr
    sublistas = []
    tamaño = len(arr) // k
    for i in range(k):
        inicio = i * tamaño
        fin = (i + 1) * tamaño if i != k - 1 else len(arr)
        sublistas.append(sorted(arr[inicio:fin]))
    # Mezcla todas las sublistas ordenadas
    import heapq
    return list(heapq.merge(*sublistas))

print("Balanced Multiway Merging:", balanced_multiway_merge([5, 2, 9, 1, 5, 6, 8, 7, 3]))


