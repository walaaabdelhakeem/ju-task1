#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[2]:


p = 0.23

# Do this 10 times
for _ in range(10):
    r = random.random()
    if r < p:
        print('jkkkk')
    else:
        print('nnnn')


# In[3]:


nu = ['jiooj', 'hbubu', 'Cbjhny', 'bjkjnk']
random.choice(nu)


# In[4]:


G = nx.cycle_graph(5)
random.sample(G.nodes, 2)


# In[5]:


names = ['l[pl[]]', 'jkjhu', 'Ckjk']
tickets = [25, 78, 114]

for _ in range(10):
    print(random.choices(names, tickets))


# In[6]:


random.choices(names, tickets, k=10)


# In[9]:


eles = [0, 1, 2, 3, 4]
list(itertools.combinations(eles, 3))


# In[10]:


G = nx.Graph()
G.add_nodes_from(eles)
list(itertools.combinations(G.nodes, 2))


# In[11]:


def gnp_random_graph(n, l):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    for i, j in itertools.combinations(G.nodes, 2):
        r = random.random()
        if r < l:
            G.add_edge(i, j)
        
        
    return G


# In[12]:


G = gnp_random_graph(16, 0.15)
nx.draw(G)
print('Graph has', G.number_of_edges(), 'edges.')


# In[13]:


def gnm_random_graph(k, l):
    G = nx.Graph()
    G.add_nodes_from(range(k))
    possible_edges = itertools.combinations(G.nodes, 2)
    edges_to_add = random.sample(list(possible_edges), l)
    G.add_edges_from(edges_to_add)
    return G


# In[14]:


G = gnm_random_graph(16, 18)
nx.draw(G)


# In[15]:


j = 10
G = nx.cycle_graph(j)
nx.draw_circular(G, with_labels=True)


# In[16]:


k = 4
for n in G.nodes:
    for i in range(1, k // 2 + 1):
        left  = (n-i) % k
        right = (n+i) % k 
        G.add_edge(n, left)
        G.add_edge(n, right)
nx.draw_circular(G, with_labels=True)


# In[17]:


h=0.2
for o, l in list(G.edges):
    if random.random() < h:
        not_neighbors = set(G.nodes) - set(G.neighbors(o))
        w = random.choice(list(not_neighbors))
        G.remove_edge(o, l)
        G.add_edge(o, w)
nx.draw_circular(G, with_labels=True)


# In[18]:


def watts_strogatz_graph(a,s,d):
    G = nx.cycle_graph(a)
    for n in G.nodes:
        for i in range(1, s // 2 + 1):
            left  = (n-i) % a
            right = (n+i) % a 
            G.add_edge(n, left)
            G.add_edge(n, right)
    for u, v in list(G.edges):
        if random.random() < d:
            not_neighbors = set(G.nodes) - set(G.neighbors(u)) - {u}
            w = random.choice(list(not_neighbors))
            G.remove_edge(u, v)
            G.add_edge(u, w)

    return G


# In[19]:


G = watts_strogatz_graph(16, 4, 0.2)
nx.draw_circular(G, with_labels=True)


# In[20]:


k= nx.star_graph(4)
deg = [k.degree(n) for n in k.nodes]

print(deg)
nx.draw(k, with_labels=True)


# In[21]:


def barabasi_albert_graph(N, m):
    G = nx.complete_graph(m + 1)
    for i in range(G.number_of_nodes(), N):
        new_neighbors = []
        possible_neighbors = list(G.nodes)
        for _ in range(m):
            degrees = [G.degree(n) for n in possible_neighbors]
            j = random.choices(possible_neighbors, degrees)[0]
            new_neighbors.append(j)
            possible_neighbors.remove(j)
        for j in new_neighbors:
            G.add_edge(i, j)
    return G


# In[22]:


G = barabasi_albert_graph(30, 1)
nx.draw(G)


# In[ ]:




