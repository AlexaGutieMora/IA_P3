# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 16:04:03 2025

@author: k
"""
############### ORDENAMIENTO DE ARBOL 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar(root, valor):
    if root is None:
        return Nodo(valor)
    if valor < root.valor:
        root.izq = insertar(root.izq, valor)
    else:
        root.der = insertar(root.der, valor)
    return root

def inorden(root, resultado):
    if root:
        inorden(root.izq, resultado)
        resultado.append(root.valor)
        inorden(root.der, resultado)

def tree_sort(arr):
    root = None
    for num in arr:
        root = insertar(root, num)
    resultado = []
    inorden(root, resultado)
    return resultado

print("Tree Sort:", tree_sort([5, 2, 9, 1, 5, 6]))
