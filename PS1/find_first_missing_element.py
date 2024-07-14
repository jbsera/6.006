# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:51:38 2022

@author: joyse
"""

##################################################
##  Problem 3.4. Find order
##################################################

# Given a list of positive integers and the starting integer d, return x such that x is the smallest value greater than
# or equal to d that's not present in the list
# def find_first_missing_element(arr, d):
#     '''
#     Inputs: 
#         arr        (list(int)) | List of sorted, unique positive integer order id's
#         d          (int)       | Positive integer of smallest possible value in arr
#     Output: 
#         -          (int)       | The smallest integer greater than or equal to d that's not present in arr
#     '''
#     ##################
#     # YOUR CODE HERE #
#     ################## 
#     if d not in arr:
#         return d
#     else:
#         for index, element in enumerate(arr[0:-1]):
#             if element+1!=arr[index+1]:
#                 return element+1
#         return arr[-1]+1

def compare_before_after(D,d,j):
    if D[j]-d>j:
        return True
    else:
        return False

def find_first_missing_element(arr, d, first_call=True):
    '''
    Inputs: 
        arr        (list(int)) | List of sorted, unique positive integer order id's
        d          (int)       | Positive integer of smallest possible value in arr
    Output: 
        -          (int)       | The smallest integer greater than or equal to d that's not present in arr
    '''
    ##################
    # YOUR CODE HERE #
    ################## 
    if first_call:
        if arr==[]:
            return d
        elif arr[-1]-d==len(arr)-1:
            return arr[-1]+1
        elif d<arr[0]:
            return d
    p_1=0
    p_2=len(arr)-1
    mid_point=(p_2-p_1)//2 + p_1
    if mid_point==p_1:
        return arr[p_1]+1
    answer=compare_before_after(arr, arr[0], mid_point)
    if answer:
        return find_first_missing_element(arr[p_1: mid_point+1], d, False)
    else:
        return find_first_missing_element(arr[mid_point:], d, False)
        
