# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 17:38:34 2025

@author: k
"""
#################NATURAL MERGING
def natural_merge_sort(arr):
    while True:
        runs = []
        n = len(arr)
        i = 0
        while i < n:
            run = [arr[i]]
            i += 1
            while i < n and arr[i - 1] <= arr[i]:
                run.append(arr[i])
                i += 1
            runs.append(run)

        if len(runs) == 1:
            return runs[0]

        arr = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                arr += merge(runs[i], runs[i + 1])
            else:
                arr += runs[i]

print("Natural Merging:", natural_merge_sort([5, 2, 9, 1, 5, 6]))
