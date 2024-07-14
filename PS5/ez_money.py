# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:31:38 2022

@author: joyse
"""

import math


def bellman_ford(Adj, w, s):
    infinity=float('inf')
    d=[infinity for _ in Adj]
    parent=[None for _ in Adj]
    d[s], parent[s]=0,s
    V=len(Adj)
    for i in range(V-1):
        for u in range(V):
            for v in Adj[u]:
                if d[v]>d[u] + w[(u,v)]:
                    d[v]=d[u] + w[(u,v)]
                    parent[v]=u
    for u in range(V):
        for v in Adj[u]:
            if d[v]>d[u]+w[(u,v)]:
                return True
    return False
    
    
def make_Adj_and_weights(D):
    items=[]
    num_to_item={}
    item_to_num={}
    weights={}
    #Creating dictionary mapping numbers/indexes to items
    for deal in D:
        if deal[0] not in items:
            items.append(deal[0])
        if deal[2] not in items:
            items.append(deal[2])
    num=0
    for item in items:
        num_to_item[num]=item
        item_to_num[item]=num
        num+=1
    #Create adjacency list and weight list
    Adj_list=[]
    for i in range(num):
        Adj_list.append([])

    for deal in D:
        A=deal[0]
        B=deal[2]
        weight=-1*math.log(deal[3]/deal[1], 2)
        Adj_list[item_to_num[A]].append(item_to_num[B])
        weights[(item_to_num[A], item_to_num[B])]=weight
    source_node=len(Adj_list)
    item_to_num['source']=source_node
    num_to_item[source_node]='source'
    source_list=[]
    for num in range(num):
        source_list.append(num)
        weights[(source_node, num)]=0
    Adj_list.append(source_list)
    return Adj_list, weights, num_to_item, item_to_num
        
        


def ez_money(D):
    """Determine if there is a sequence of commodities to exchange
    to get more of some commodity than you started with.

    Args:
        D: A list of deals, where each is of the form (A, x, B, y),
           meaning that someone will give you y of B for x of A.
           'A' and 'B' are strings, and 'x' and 'y' are integers.

    Returns:
        True if such an opportunity exists, False otherwise.
    """

    Adj, Weights, num_to_item, item_to_num= make_Adj_and_weights(D)
    start=item_to_num['source']
    return bellman_ford(Adj, Weights, start)


    
    