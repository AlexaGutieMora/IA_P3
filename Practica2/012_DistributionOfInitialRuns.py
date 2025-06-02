# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 18:10:20 2025

@author: k
"""
################# DISTRIBUTION OF INITIAL RUNS
def distribuir_runs(arr):
    tapes = [[], []]
    run, idx = [arr[0]], 0

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            run.append(arr[i])
        else:
            tapes[idx].append(run)
            run = [arr[i]]
            idx ^= 1  #Alterna entre 0 y 1
    tapes[idx].append(run)
    return tapes

t1, t2 = distribuir_runs([5, 7, 8, 2, 3, 9, 1, 4])
print("Cinta 1:", t1)
print("Cinta 2:", t2)
