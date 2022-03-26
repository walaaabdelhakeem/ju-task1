#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello ')


# In[3]:


mstr = 'H'
mint = 1

print(mstr)
print(mint)


# In[4]:


num=5
if num<1:
    print('<1')
elif num==1:
    print('=1')
else:
    print('no')


# In[11]:


sname=['walaa','aml','mama']

print(sname[1])
print(sname[-1])
print(sname[1:2])
print(sname[:2])
print(sname[0:])


# In[25]:


sname.append('ss')
print(sname)


# In[21]:


sname.insert(2,'s')
print(sname)


# del sname[2]
# print(sname)

# In[23]:


del sname[2] 
print(sname)


# In[26]:


sname.append('m')
sname.append('m')
print(sname)


# In[27]:


name=['dd','sam','nany']
for i in name:
    print(i)


# In[30]:


long=[]
for i in name:
    if len(name)<5:
        long.append(i)
print(long)


# In[35]:


a=[]
name=['dd','sam','nany']
for i in name:
    for j in name:
        a.append((i,j))
print(a)


# In[36]:


print(name[0])


# In[39]:


a=[]
name=['dd','sam','nany']
for i in name:
    for j in name:
        if i!=j:
            a.append((i,j))
print(a)


# In[40]:


grade=('wala','st','f-')
print(grade)


# In[41]:


print(grade[0])


# In[45]:


print(grade.append('hhh'))


# In[46]:


del grade[2]


# In[47]:


grade=('waa','asa','dsd')
name,sub,g=grade
print(g)
print(name)
print(sub)


# In[48]:


for i in grade:
    if i[2].startswith('A'):
        print('Congratulations', i[0],
              'on getting an', i[2],
              'in', i[1])


# In[49]:


languages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}


# In[50]:


for i in languages:
    v=languages[i]
    print(i,v)


# In[53]:


grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]
records = []
for i,j,k in grades:
    record = {
        'name': i,
        'subject': j,
        'grade': k,
    }
    records.append(record)
    
records


# In[ ]:





# In[ ]:




