#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


df1=pd.read_csv('NIFTY50_all.csv')


# In[7]:


df1.head()


# In[8]:


df1.tail()


# In[9]:


df2=pd.read_csv('stock_metadata.csv')


# In[10]:


df2.head()


# In[12]:


df=pd.merge(df1,df2,on='Symbol',how='outer')


# In[13]:


df


# In[14]:


df.to_csv('merged_file.csv', index=False)


# In[15]:


df=pd.read_csv('merged_file.csv')


# In[16]:


df['% Change']=(df['Close']-df['Open'])/df['Open']*100


# In[17]:


df.to_csv('merged_file.csv', index= False)


# In[ ]:




