#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns


# In[3]:


flights=sns.load_dataset("Flights")


# In[4]:


flights


# In[5]:


flights.head()


# In[6]:


flights=flights.pivot("month","year","passengers")


# In[7]:


flights.head()


# In[9]:


sns.heatmap(flights)


# In[10]:


sns.heatmap(flights,annot=True)


# In[12]:


sns.heatmap(flights,annot=True,fmt="d")


# In[13]:


sns.heatmap(flights,annot=True,fmt="d",cmap='RdBu')


# In[20]:


sns.heatmap(flights,annot=True,fmt="d",cmap='RdBu',linewidth=0.9)


# In[21]:


###
tips=sns.load_dataset("tips")


# In[22]:


tips


# In[23]:


tips.head()


# In[29]:


sns.barplot(x='day',y='tip',data=tips)


# In[30]:


sns.barplot(x='day',y='tip',data=tips,hue="sex")


# In[33]:


sns.barplot(x='day',y='tip',data=tips,hue="sex",palette="winter")


# In[ ]:




