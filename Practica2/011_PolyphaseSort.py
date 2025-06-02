# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 17:59:31 2025

@author: k
"""
#################### POLYPHASE SORT
def polyphase_sort(arr):
    tapes = [[x] for x in sorted(arr)] #series parciales
    while len(tapes) > 1:
        a = tapes.pop(0)
        b = tapes.pop(0)
        tapes.append(merge(a, b)) #se mezcla progresivamente
    return tapes[0]

print("Polyphase sort:", polyphase_sort([5, 2, 9, 1, 5, 6]))

