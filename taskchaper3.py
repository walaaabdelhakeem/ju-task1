#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[6]:


G = nx.read_edgelist('ia-enron-only.edges', nodetype=int)
print(nx.info(G))
nx.draw(G)


# In[7]:


max([1,2,3,4,5])


# In[9]:


max(['assdsf', 'fdsgdfh', 'ddsg'])


# In[11]:


max(['assdsf', 'fdsgdfh', 'ddsg'],key=len)


# In[12]:


high = max(G.nodes, key=G.degree)
high


# In[13]:


G.degree(high)


# In[14]:


betweenness = nx.centrality.betweenness_centrality(G)
highest_betweenness_node = max(G.nodes, key=betweenness.get)
highest_betweenness_node


# In[15]:


betweenness[highest_betweenness_node]


# In[16]:


max(G.nodes, key=betweenness)


# In[17]:


degree = [G.degree(n) for n in G.nodes]


# In[18]:


import statistics

print('Mean degree:', statistics.mean(degree))
print('Median degree:', statistics.median(degree))


# In[21]:


betweenness = nx.centrality.betweenness_centrality(G)
betweenness_sequence = list(betweenness.values())

print('Mean betweenness:', statistics.mean(betweenness_sequence))
print('Median betweenness:', statistics.median(betweenness_sequence))


# In[23]:


from collections import Counter

degree = Counter(degree)
degree


# In[26]:


min_degree, max_degree = min(degree.keys()), max(degree.keys())
x = list(range(min_degree, max_degree + 1))


# In[27]:


y = [degree.get(x, 0) for x in plot_x]


# In[28]:


import matplotlib.pyplot as plt
plt.bar(x,y)


# In[29]:


counts, bins, patches = plt.hist(betweenness_sequence, bins=10)


# In[30]:


bins


# In[31]:


counts


# In[32]:



nx.connected_components(G)


# In[33]:


c = next(nx.connected_components(G))
c


# In[34]:


len(c)


# In[35]:


com = list(nx.connected_components(G))


# In[36]:


len(com)


# In[37]:


C = G.copy()


# In[38]:


import random

nodes = random.sample(list(C.nodes), 2)
C.remove_nodes_from(nodes)


# In[41]:


num = 25
m = G.number_of_nodes() // num
m


# In[42]:


num_n = range(0, G.number_of_nodes(), m)


# In[48]:


import random
b = G.number_of_nodes()
c = G.copy()
rand = []
for nodes_removed in num_n:
    core = next(nx.connected_components(c))
    co= len(core) / b
    rand.append(co)
    if c.number_of_nodes() > m:
        nodes = random.sample(list(c.nodes), m)
        c.remove_nodes_from(nodes)


# In[49]:


plt.title('Random failure')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_n, rand, marker='o')


# In[52]:


nod = sorted(G.nodes, key=G.degree, reverse=True)
top = nod[:m]
top


# In[53]:


n = G.number_of_nodes()
number_of_steps = 25
m = n // number_of_steps

num_nodes_removed = range(0, n, m)
c = G.copy()
targeted_attack_core_proportions = []
for nodes_removed in num_nodes_removed:
    core = next(nx.connected_components(c))
    core_proportion = len(core) / n
    targeted_attack_core_proportions.append(core_proportion)
    if c.number_of_nodes() > m:
        nodes_sorted_by_degree = sorted(c.nodes, key=c.degree, reverse=True)
        nodes_to_remove = nodes_sorted_by_degree[:m]
        c.remove_nodes_from(nodes_to_remove)


# In[54]:


plt.title('Targeted attack')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, targeted_attack_core_proportions, marker='o')


# In[57]:


plt.title('Random failure vs. targeted attack')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, rand, marker='o', label='Failures')
plt.plot(num_nodes_removed, targeted_attack_core_proportions, marker='^', label='Attacks')
plt.legend()


# In[ ]:




