# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:52:32 2022

@author: joyse
"""

##################################################
##  Problem 1. common
##################################################

# Given an array of lists of distinct numbers, 
# return the number of numbers common to all lists

def common(lists):
    '''
    Input:  lists  | Array of arrays of positive integers
    Output: num_common  | number of numbers common to all arrays
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    num_common = 0
    #Only care about non-empty lists
    if lists!=[]:
        #If length one, return length
        if len(lists)==1 and lists[0]!=[]:
            num_common=len(lists[0])

        #Restrain common numbers by the first list   
        common_numbers=lists[0]
        
        #Iterate through common numbers and check if in list1, if not remove from common_numbers
        for list1 in lists[1:]:
            common_copy=common_numbers.copy()
            for num in common_copy:
                if num not in list1:
                    common_numbers.remove(num)
        num_common=len(common_numbers)
        
  
    return num_common

