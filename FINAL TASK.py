#!/usr/bin/env python
# coding: utf-8

# In[1]:


#t/1
import networkx as nx
h = nx.Graph()
h.add_nodes_from([1,2,3,4,5,6])
h.add_edges_from([(1,2),(1, 3), (1, 4), (1, 6),(2,3),(2,4),(3,6)])
nx.draw(h, with_labels=True,node_color='red',
        node_size=1000,
        font_color='white')


# In[2]:


def plot_degree_dist(h):
    
    degrees = h.degree()
    deg = dict(degrees)
    v = sorted(set(deg.values()))
    print(v)
    ss = [list(deg.values()).count(x) for x in v]
    p = [x / h.order() for x in ss]
    print(len(p))
    
    plt.figure()
    plt.bar(v, p)
    plt.xlabel("k",fontsize=20)
    plt.ylabel("p(k)", fontsize=20)
    plt.title("Degree Distribution", fontsize=20)
    
    plt.show()
    plt.figure()
    plt.grid(False)
    plt.loglog(v, p, "bo")
    plt.xlabel("k", fontsize=20)
    plt.ylabel("log p(k)", fontsize=20)
    plt.title("log Degree Distribution")
    plt.show()
    plt.show() 


# In[4]:


from collections import Counter
import matplotlib.pyplot as plt
d_s = [h.degree(n) for n in h.nodes]
d_c = Counter(d_s)
mi_d, mx_d = min(d_c.keys()), max(d_c.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Number of Nodes", fontsize=20)
a = list(range(mi_d, mx_d + 1))
z = [d_c.get(x, 0) for x in a]
plt.bar(a, z)


# In[5]:


g = nx.adjacency_matrix(h) 


# In[6]:


print(g.todense())


# In[7]:


#t/2
G = nx.DiGraph()
G.add_nodes_from([1,2,3,4,5,6])
G.add_edges_from([
    (1,2),
    (2,3),(2,4),
    (3,1), (3,2),
    (4,1),
    (6,1),
    (6,3),
])
nx.draw(G, with_labels=True,node_color='#283618',
        node_size=1000)


# In[8]:


def plot_degree_dist(h):
    
    degrees = G.degree()
    deg = dict(degrees)
    v = sorted(set(deg.values()))
    print(v)
    SS = [list(deg.values()).count(x) for x in v]
    P = [x / G.order() for x in SS]
    print(len(P))
    
    plt.figure()
    plt.bar(v, P)
    plt.xlabel("k",fontsize=20)
    plt.ylabel("p(k)", fontsize=20)
    plt.title("Degree Distribution", fontsize=20)
    
    plt.show()
    plt.figure()
    plt.grid(False)
    plt.loglog(v, P, "bo")
    plt.xlabel("k", fontsize=20)
    plt.ylabel("log p(k)", fontsize=20)
    plt.title("log Degree Distribution")
    plt.show()
    plt.show()  


# In[9]:


from collections import Counter
degree_sequence = [G.degree(n) for n in G.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Number of Nodes", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[10]:


N = nx.adjacency_matrix(G) 


# In[11]:


print(N.todense())


# In[ ]:




