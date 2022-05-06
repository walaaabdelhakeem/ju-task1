#!/usr/bin/env python
# coding: utf-8

# In[23]:


#chapter 1, 2
#Exarsais1 chater1
import networkx as nx
G=nx.Graph()
print(open('friends.adjlist').read())


# In[24]:


SG = nx.read_adjlist('friends.adjlist')


# In[25]:


nx.draw(SG, node_size=1500, node_color='blue', with_labels=True)


# In[26]:


#Exarsais2 chater1
def max_degree(n):
    max1=0
    list1=[]
   
    for i in n.nodes:
        if n.degree(i)>max1:
            max1=n.degree(i)
            nm=i
    list1.append(nm)
    list1.append(max1)
    print(list1)
max_degree(SG)


# max_dgree(SG)

# In[27]:


def mutual_friends(n, node_1, node_2):
    list1=[]
    list2=list(n.neighbors(node_1))
    list3=list(n.neighbors(node_2))
    for i in range(len(list2)):
        for j in range(len(list3)):
            if list2[i]==list3[j]:
                list1.append(list2[i])
    print(list1)
mutual_friends(SG, 'Alice', 'Claire')


# In[71]:


import networkx as nx
get_ipython().run_line_magic('matplotlib', 'inline')


# In[72]:


nx.__version__


# In[73]:



G = nx.Graph()


G.add_node('amal')

nodes_to_add = ['sd', 'df', 'asa']
G.add_nodes_from(nodes_to_add)


G.add_edge('amal', 'sd')


edges_to_add = [('amal', 'df'), ('sd', 'df'), ('df', 'asa')]
G.add_edges_from(edges_to_add)


nx.draw(G, with_labels=True)


# In[74]:


nx.draw(G,
        with_labels=True,
        node_color='red',
        node_size=2000,
        font_color='blue',
        font_size=20,
        )


# In[75]:


G.nodes()


# In[76]:


G.edges()


# In[77]:


for node in G.nodes:
    print(node)


# In[78]:


for edge in G.edges:
    print(edge)


# In[79]:


G.number_of_nodes()


# In[80]:



G.number_of_edges()


# In[81]:


G.neighbors('sd')


# In[82]:


for neighbor in G.neighbors('sd'):
    print(neighbor)


# In[83]:


list(G.neighbors('df'))


# In[84]:


nx.is_tree(G)


# In[85]:



nx.is_connected(G)


# In[86]:


G.has_node('amal')


# In[87]:


G.has_node('j')


# In[88]:


'asa' in G.nodes


# In[89]:


G.has_edge('amal', 'df')


# In[90]:


G.has_edge('amal', 'asa')


# In[91]:


('df', 'asa') in G.edges


# In[92]:


len(list(G.neighbors('amal')))


# In[93]:


G.degree('amal')


# In[94]:


items = ['walaa', 'om', 'up']
[item.upper() for item in items]


# In[95]:


print(G.nodes())
print([G.degree(n) for n in G.nodes()])


# In[96]:


g = (len(item) for item in items)
list(g)


# In[97]:


max(len(item) for item in items)


# In[98]:


sorted(item.upper() for item in items)


# In[99]:


G = nx.Graph()

G.add_nodes_from(['cat','go','us',13])

G.add_edge('cat','go')

nx.draw(G, with_labels=True, font_color='red', node_size=1500)


# In[100]:


D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(D, with_labels=True)


# In[101]:


D.has_edge(1,2)


# In[102]:


D.has_edge(1,2)


# In[103]:


print('Successors of 2:', list(D.successors(2)))

print('Predecessors of 2:', list(D.predecessors(2)))


# In[104]:


D.degree(2)


# In[105]:


print('Successors of 2:', list(D.successors(2)))
print('"Neighbors" of 2:', list(D.neighbors(2)))


# In[106]:


#chapter(2)
G = nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])

nx.draw(G, with_labels=True)


# In[107]:


nx.has_path(G, 3, 4)


# In[108]:


list(nx.all_simple_paths(G, 3, 4))


# In[109]:


nx.shortest_path(G, 3, 4)


# In[110]:


G = nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])

nx.draw(G, with_labels=True)


# In[111]:


nx.has_path(G, 3, 4)


# In[113]:


G = nx.Graph()

nx.add_cycle(G,(1,2,3))
G.add_edge(4,5)

nx.draw(G, with_labels=True)


# In[114]:


nx.shortest_path_length(G, 3, 4)


# In[115]:


nx.shortest_path(G, 3, 4)


# In[116]:


nx.has_path(G, 3, 5)


# In[117]:


import networkx as nx
get_ipython().run_line_magic('matplotlib', 'inline')


# In[118]:


G = nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])

nx.draw(G, with_labels=True)


# In[119]:


list(nx.all_simple_paths(G, 3, 4))


# In[120]:



nx.shortest_path(G, 3, 4)


# In[121]:


nx.shortest_path_length(G, 3, 4)


# In[122]:


nx.is_connected(G)


# In[123]:


G = nx.Graph()

nx.add_cycle(G,(1,2,3))
G.add_edge(4,5)

nx.draw(G, with_labels=True)


# In[124]:



nx.is_connected(G)


# In[125]:


nx.has_path(G, 3, 5)


# In[127]:


nx.has_path(G, 3, 5)


# In[128]:



nx.number_connected_components(G)


# In[129]:


list(nx.connected_components(G))


# In[130]:


components = list(nx.connected_components(G))
len(components[0])


# In[131]:


max(nx.connected_components(G), key=len)


# In[132]:


nodes = max(nx.connected_components(G), key=len)
co = G.subgraph(nodes)

nx.draw(co, with_labels=True)


# In[133]:


has = nx.DiGraph()
has.add_edges_from([
    (1,2),
    (2,3),
    (3,2), (3,4), (3,5),
    (4,2), (4,5), (4,6),
    (5,6),
    (6,4),
])
nx.draw(has, with_labels=True)


# In[134]:


nx.has_path(has, 1, 4)


# In[135]:


nx.has_path(has, 4, 1)


# In[136]:


nx.shortest_path(has, 2, 5)


# In[138]:


nx.shortest_path(has, 5, 2)


# In[139]:


nx.is_weakly_connected(has)


# In[140]:


nx.is_connected(has)


# In[141]:


list(nx.weakly_connected_components(has))


# In[142]:


list(nx.strongly_connected_components(D))


# In[149]:


G = nx.read_graphml('openflights_usa.graphml.gz')


# In[150]:


G.nodes['IND']


# In[151]:


G.nodes['IND']['name']


# In[153]:


#Exarsais1 chater2

ini=list(nx.shortest_path(G,'IND','FAI'))
if len(ini)==2:
    print('yes')
else:
    print('no')


# In[154]:


#Exarsais2 chater2
nx.shortest_path(G,'IND','FAI')


# In[158]:


#Exarsais3 chater2
def connecting_flights(G):
    ls=[]
    f=0
    for n in G.nodes:
        ls.append(n)
    for i in range(len(ls)):
        for j in range(len(ls)):
            if nx.has_path(G,ls[i],ls[j]):
                continue
            else:
                f=1
                break
    if f==0:
        print('yes')
    else:
        print("no")
connecting_flights(G)
                    


# In[ ]:




