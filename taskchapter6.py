#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[5]:


G = nx.Graph()
nx.add_cycle(G,[0, 1, 2, 3])
nx.add_cycle(G,[4, 5, 6, 7])
G.add_edge(0, 7)

nx.draw(G, with_labels=True)


# In[8]:


part = [
    {1, 2, 3},
    {4, 5, 6},
    {0, 7},
]


# In[11]:


nx.community.is_partition(G, part)


# In[13]:


mmap = {}
for idx, cluster_nodes in enumerate(part):
    for node in cluster_nodes:
        mmap[node] = idx
mmap


# In[14]:


nodes = [mmap[n] for n in G.nodes]       
nx.draw(G, node_color=nodes, with_labels=True)


# In[24]:


def modularity(G, part):
    W = sum(G.edges[v, w].get('weight', 1) for v, w in G.edges)
    summation = 0
    for cluster_nodes in part:
        s_c = sum(G.degree(n, weight='weight') for n in cluster_nodes)
        C = G.subgraph(cluster_nodes)
        W_c = sum(C.edges[v, w].get('weight', 1) for v, w in C.edges)
        summation += W_c - s_c ** 2 / (4 * W)
    return summation / W


# In[25]:


modularity(G, part)


# In[26]:


part_2 = [
    {0, 1, 2, 3},
    {4, 5, 6, 7},
]
modularity(G, part_2)


# In[27]:


nx.community.quality.modularity(G,part_2)


# In[28]:


p = nx.karate_club_graph()
nx.draw(p, with_labels=True)


# In[30]:


p.nodes[0]


# In[37]:


K = nx.karate_club_graph()
club_color = {
    'Mr. Hi': 'orange',
    'Officer': 'lightblue',
}
node_colors = [club_color[K.nodes[n]['club']] for n in K.nodes]
nx.draw(K, node_color=node_colors, with_labels=True)


# In[39]:


groups = {
    'Mr. Hi': set(),
    'Officer': set(),
}

for i in K.nodes:
    club = K.nodes[i]['club']
    groups[club].add(i)
    
groups


# In[41]:


emp = list(groups.values())
emp


# In[42]:


nx.community.is_partition(K, emp)


# In[43]:


nx.community.quality.modularity(K, emp)


# In[47]:


randomns = random.sample(K.nodes, 17)
randomn = [set(randomns),
                    set(K.nodes) - set(randomns)]
randomn


# In[52]:


random_colors = ['orange' if n in randomns else 'lightblue' for n in K.nodes]
nx.draw(K, node_color=random_colors)


# In[53]:


nx.community.quality.modularity(K, randomn)


# In[54]:


G = nx.karate_club_graph()
nx.draw(G)


# In[55]:


nx.edge_betweenness_centrality(G)


# In[56]:


my = nx.edge_betweenness_centrality(G)
my[0, 1]


# In[57]:


my.get((0, 1))


# In[58]:


max(my, key=my.get)


# In[59]:


max(G.edges(), key=my.get)


# In[60]:


bb= nx.edge_betweenness_centrality(G)
most = max(G.edges(), key=bb.get)
G.remove_edge(*most)


# In[61]:


nx.connected_components(G)


# In[62]:


list(nx.connected_components(G))


# In[63]:


G = nx.karate_club_graph()
part = []
for _ in range(G.number_of_edges()):
    my = nx.edge_betweenness_centrality(G)
    most = max(G.edges(), key=my.get)
    G.remove_edge(*most)
    my_partition = list(nx.connected_components(G))
    part.append(my_partition)


# In[64]:


len(part), nx.karate_club_graph().number_of_edges()


# In[65]:


len(part[0])


# In[67]:


len(part[-1]), nx.karate_club_graph().number_of_nodes()


# In[68]:


G = nx.karate_club_graph()
mod = [modularity(G, p) for p in part]
mod


# In[69]:


import matplotlib.pyplot as plt
plt.plot(mod)
plt.ylabel('Modularity')
plt.xlabel('Algorithm step')


# In[74]:


best_partition = max(part, key=nx.community.quality.modularity)


# In[76]:


def my_modularity(partition):
    return nx.community.quality.modularity(G, partition)
best_partition = max(part, key=my_modularity)
best_partition


# In[77]:


def create_partition_map(partition):
    partition_map = {}
    for idx, cluster_nodes in enumerate(partition):
        for node in cluster_nodes:
            partition_map[node] = idx
    return partition_map


# In[78]:


best_partition_map = create_partition_map(best_partition)

node_colors = [best_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)


# In[79]:


nx.community.quality.modularity(G, best_partition)


# In[80]:


for partition in part:
    if len(partition) == 2:
        two_n = partition
        break

two_n


# In[83]:


two_map = create_partition_map(two_n)

node_colors = [two_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)


# In[84]:


nx.community.quality.modularity(G, two_n)


# In[85]:


import matplotlib.pyplot as plt

pos = nx.layout.spring_layout(G)
fig = plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
two_map = create_partition_map(two_n)
node_colors = [two_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('sdgsdvd')

plt.subplot(1, 2, 2)
node_colors = [G.nodes[n]['club'] == 'Officer' for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('fsdddg')


# In[86]:


G.nodes[8]


# In[87]:


list(nx.community.girvan_newman(G))[:5]


# In[ ]:




