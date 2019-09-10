#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import seaborn as sns


# In[4]:


import matplotlib.pyplot as plt
plt.style.use('classic')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df = pd.read_csv("C:\DataSets\gun-violence-data_01-2013_03-2018.csv")


# In[6]:


df


# In[7]:


df.head()


# In[8]:


incident_occurance = df.state.value_counts(sort=True, ascending=False)


# In[9]:


incident_occurance


# In[10]:


# so those were the states with most incidents


# In[11]:


incident_occurance.head()


# In[12]:


# ill read those values into a file for the ease of access


# In[13]:


df1 = pd.read_csv("C:\DataSets\sample.csv")


# In[14]:


df1


# In[15]:


# So these are the states with most occurance of  incidents


# In[16]:


df1.head(8)


# In[37]:


df3= df1.iloc[:16]


# In[38]:


df3


# In[77]:


import matplotlib.pyplot as plt
import numpy as np

def scatterplot(incid, states, x_label="incident", y_label="states", title="States with Most Incidents", color = "r", yscale_log=False):

    # Create the plot object
    _, df3 = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    df3.scatter(incid, states, s=df3['c']*1200 , color = color, alpha = 1.75)

    if yscale_log == True:
        df3.set_yscale('log')

    # Label the axes and provide a title
    df3.set_title(title)
    df3.set_xlabel(incid)
    df3.set_ylabel(states)


# In[78]:


sns.scatterplot(df3.incid, df3.states)


# In[47]:


incident = incident_occurance.head(16)


# In[50]:


# It can be seen the same comparison of number of states which has got highest number of incidents as a horizontal bar graph just for different visuals


# In[51]:


incident


# In[52]:


incident.plot(kind='barh')


# In[53]:


# scatter plot and horizontal bar graphs which show the states of US with the maximum number of incidents in the mass
# shooting over the years 2013-2018


# In[54]:


p_age = df.participant_age.value_counts(sort=True, ascending=False)


# In[55]:


p_age


# In[56]:


# These are the participants ages regarding to the number of incidents those aged participants have committed


# In[57]:


df4 = pd.read_csv("C:\DataSets\participantsage.csv")


# In[58]:


df4


# In[59]:


df4 = df4.cumsum()


# In[60]:


plt.figure()


# In[61]:


df4.plot()


# In[62]:


# The number of incidents series for teens are observed to be too low
# and for the people who are aged somewhere around 30's have got the maximum


# In[64]:


df5 = df.groupby(['n_injured', 'state']).mean()


# In[65]:


df5


# In[66]:


# By Calling this function it usually gives out the tabulated values giving high consideration to state and number of injured


# In[67]:


df6 = dt.tail(22)


# In[68]:


df6


# In[69]:


# so now mainly focussing on the states with the most number of injuries therefore by selecting the values from the bottom


# In[70]:


df7 = pd.read_csv("C:\DataSets\inj.csv")


# In[71]:


df7


# In[73]:


# by calling the csv files which does contain the datas of number of people being highly injured among the states and also
# the probablity of kills among those incidents


# In[74]:


import seaborn as sns


# In[76]:


ax = sns.regplot(df7.n_injured, df7.n_killed)


# In[80]:


#This is the scatter plot with the regression line, which visually shows the majority of the values are somewhere
# near where the regression line is passing by. The plot defines based on the states, the most number of injuries
# and based on that injuries, the probablity of them to be killed.


# In[ ]:




