#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r"C:\Users\mayan\Downloads\FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding = "latin-1")
df.groupby('Element').first()


# In[2]:


df.groupby('Item').sum()


# In[3]:


df.isnull().sum()


# In[4]:


my_tuppy = (1,2,5,8)

my_tuppy[2] = 6


# In[ ]:




