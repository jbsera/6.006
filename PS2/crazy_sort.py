# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:09:30 2022

@author: joyse
"""
import math


def crazy_sort(A,i,j):
    n=j-i
    if n<=1:
        return
    if n==2: 
        # print('i', i, 'j', j)
        # print('A initial', A)
        A[i], A[j-1]=min(A[i:j]), max(A[i:j])
        print('A here', A)
        return
    m=math.floor(2.0*n/3.0)
    crazy_sort(A, i, i+m)
    crazy_sort(A, j-m, j)
    crazy_sort(A, i, i+m)
    # print("A", A)
    
A=[8,7,6,5,4,3,2,1]
print(crazy_sort(A, 0, 8))
print(A)

        