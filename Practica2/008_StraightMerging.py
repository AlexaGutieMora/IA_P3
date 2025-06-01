# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 17:30:35 2025

@author: k
"""

########################STRAIGHT MERGING
def straight_merge_sort(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2
    return arr

print("Straight merging:", straight_merge_sort([5, 2, 9, 1, 5, 6]))
