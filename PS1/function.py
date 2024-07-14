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
def find_first_missing_element(arr, d):
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
    if d not in arr:
        return d
    else:
        for index, element in enumerate(arr[0:-1]):
            if element+1!=arr[index+1]:
                return element+1
        return arr[-1]+1
            
    
#print(find_first_missing_element([1, 2, 3, 4, 5, 6], 1))