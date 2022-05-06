#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[2]:


def initial_state(G):
    s = {}
    for node in G.nodes:
        s[node] = 'asleep'
    return s


# In[3]:


initial_state(G)


# In[4]:


import random

P_AWAKEN = 0.2
def state_transition(G, current_state):
    nextb = {}
    for node in G.nodes:
        if current_state[node] == 'asleep':
            if random.random() < P_AWAKEN:
                nextb[node] = 'awake'
    return nextb


# In[5]:


te = initial_state(G)
state_transition(G, te)


# In[6]:


from simulation import Simulation

sim = Simulation(G, initial_state, state_transition, name='Simple Sim')


# In[7]:


sim.state()


# In[8]:


sim.draw()


# In[9]:


sim.run()


# In[10]:


sim.steps
sim.draw(with_labels=True)


# In[11]:


sim.state()


# In[12]:


sim.run(10)
sim.steps


# In[13]:


sim.draw(with_labels=True)


# In[14]:


sim.plot()


# In[15]:


sim.draw(4, with_labels=True)


# In[16]:


sim.state(4)


# In[17]:


sim.plot(min_step=2, max_step=8)


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[19]:


import random
import string

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = random.choice('ABCD')
    return state


# In[20]:



initial_state(G)


# In[21]:


def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        # Caveat: what if the node has no neighbors?
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[22]:


tte = initial_state(G)
state_transition(G, tte)


# In[23]:


import matplotlib.pyplot as plt

sim = Simulation(G, initial_state, state_transition, name='Voter Model')
sim.draw()


# In[24]:


sim.run(40)
sim.draw()


# In[25]:


sim.plot()


# In[26]:


import random
def state_transition(G, current_state):
    ne = {}
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            ne[node] = current_state[neighbor]
    return ne


# In[27]:


def state_transition_async(G, current_state):
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[32]:


def state_transition_async(G, current_state):
    n= list(G.nodes)
    random.shuffle(n)
    for node in n:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[33]:


sim = Simulation(G, initial_state, state_transition_async, name='Async Voter Model')
sim.run(40)
sim.plot()


# In[34]:


def stop_condition(G, current_state):
    unique_state_values = set(current_state.values())
    is_stopped = len(unique_state_values) <= 1
    return is_stopped


# In[35]:


sim = Simulation(G, initial_state, state_transition, stop_condition, name='Voter model')
sim.run(100)


# In[36]:


sim.steps


# In[37]:


sim.plot()


# In[38]:


def state_transition_async_rewiring(G, current_state):
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
            neighbor = random.choice(list(G.neighbors(node)))
            if current_state[node] != current_state[neighbor]:
                G.remove_edge(node, neighbor)
            
    return current_state


# In[39]:


sim = Simulation(G, initial_state, state_transition_async_rewiring, stop_condition,
                 name='Voter Model with rewiring')
sim.draw()


# In[40]:


sim.run(40)
sim.draw()


# In[41]:


sim.plot()


# In[42]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[43]:


import random
def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'S'
    
    patient_zero = random.choice(list(G.nodes))
    state[patient_zero] = 'I'
    return state


# In[44]:


initial_state(G)


# In[45]:


BETA = 0.1
MU = 0.1
def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'I':
            if random.random() < MU:
                next_state[node] = 'S'
        else: # current_state[node] == 'S'
            for neighbor in G.neighbors(node):
                if current_state[neighbor] == 'I':
                    if random.random() < BETA:
                        next_state[node] = 'I'

    return next_state
test_state = initial_state(G)
state_transition(G, test_state)


# In[46]:


sim = Simulation(G, initial_state, state_transition, name='SIS model')
sim.draw()


# In[47]:


sim.run(25)
sim.draw()


# In[48]:


sim.plot()


# In[ ]:




