#!/usr/bin/env python
# coding: utf-8

# In[9]:


import networkx as nx
G  =nx.Graph()
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
def get_leaves(G):
    li=[]
    for i in G.nodes():
        if G.degree(i)==1:
            li.append(i)
    return li


# In[10]:


get_leaves(G)


# In[ ]:




