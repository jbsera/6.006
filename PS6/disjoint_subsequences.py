# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:14:00 2022

@author: joyse
"""

def disjoint_subsequences(X, Y):
    """Determine whether X appears as a sub-sequence of Y twice, where the two
    sub-sequences are disjoint. In addition to the usual alphanumeric
    characters, Y may contain instances of the special wild card character '*'
    that can match any other character.

    Args:
        X: a string
        Y: a string

    Returns:
        True if X appears as a sub-sequence of Y twice.
    """
    if Y=='':
        return False
    k=len(X)
    n=len(Y)
    T={}

    def memo(i,j,z):
        ###BASE CASE
        if z==n:
            if i==k and j==k:
                return True
            else:
                return False

        if i!=k and z!=n and (X[i]==Y[z] or Y[z]=='*'):
            if memo(i+1,j,z+1):
                return True
        if j!=k and z!=n and (X[j]==Y[z] or Y[z]=='*'):
            if memo(i,j+1,z+1):
                return True
        elif z!=n:
            if memo(i,j,z+1):
                return True
      
        
    
    if memo(0,0,0):
        return True
    else:
        return False
    # return T[(0,0,0)]

#print(disjoint_subsequences('cat', 'catcrt'))
    

            