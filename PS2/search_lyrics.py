# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:24:29 2022

@author: joyse
"""

PRIME = 2 ** 31 - 1


def search_lyrics(L, Q):
    """
    Input: L | an ASCII string 
    Input: Q | an ASCII string where |Q| < |L|
    
    Return `True` if Q appears inside the lyrics L and `False` otherwise.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    m=len(Q)
    first_value=L[0:m]
    for index, char in enumerate(first_value):
        if index==0:
            answer=(ord(char)*128) % PRIME
        elif index==len(first_value)-1:
            answer=((answer+ord(char))) % PRIME
        else:
            answer=((answer+ord(char))*128) % PRIME
    for index, char in enumerate(Q):
        if index==0:
            Q_answer=(ord(char)*128) % PRIME
        elif index==m-1:
            Q_answer=((Q_answer+ord(char))) % PRIME
        else:
            Q_answer=((Q_answer+ord(char))*128) % PRIME
    if answer==Q_answer:
        return True
    for index in range(1, len(L)):
        if (index+m-1)<len(L):
            answer=((128*answer)-(ord(L[index-1])*(128**m))+ord(L[index+m-1]))%PRIME
            if answer==Q_answer:
                return True
    return False
    
