#!/usr/bin/env python
# coding: utf-8

# pandas

# In[6]:


import pandas as pd
import numpy as np


# In[21]:


df = pd.read_csv("chipotle.tsv", sep="\t")


# In[22]:


df.head(5)


# In[23]:


df.shape


# In[24]:


df.info()


# In[25]:


df.index


# In[27]:


df.describe(include="all")


# In[28]:


df.head()


# In[35]:


df.loc[(df.quantity==15 )|( df.item_name	=="Nantucket Nectar")]


# In[37]:


df.iloc[[9]]


# In[38]:


df.iloc[3:11]


# In[39]:


df.item_price.dtype


# In[40]:


df.item_price


# In[54]:


x=df.iloc[3:5,:-1]
y=df.iloc[3:5,-1]
print(y)


# In[62]:


df.item_price.apply(lambda x: replace('$',""))


# In[56]:


df.head()


# In[66]:


df.head(10)

