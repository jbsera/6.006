# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:20:25 2022

@author: joyse
"""
def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        order = []
        parent[s] = s
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order

def reverse_list(Adj):
    new_Adj=[]
    for i in range(len(Adj)):
        new_Adj.append([])
    for index, node in enumerate(Adj):
        for neighbor in node:
            new_Adj[neighbor].append(index)
    return new_Adj
        
        

def find_meeting_point(Adj):
    '''
    inputs:
        Adj - an adjacency list such as [[1,2], [2], []]
    return a meeting point or None if no meeting points exist
    '''
    #reverse adjacency list
    new_list=reverse_list(Adj)
    #find last node in order
    last_elm=full_dfs(new_list)[1][-1]
    #call DFS from last element
    parents=dfs(new_list, last_elm)[0]
    for parent in parents:
        if parent==None:
            return None
    return last_elm

            