#!/usr/bin/env python
# coding: utf-8

# ## Import Lib

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import re


# ## Read Data from CSV

# In[2]:


data = pd.read_csv('Desktop/Sample-click-log.csv',encoding='unicode_escape')
data.head()


# ## Check the columns in the dataframe

# In[5]:


data.columns


# ## Questions 1(a)
# For every affiliate_id(Col B), calculate the unique ios_ifa(Col K) & google_aid(Col L) present in the data.

# In[6]:


print ('Answer 1(a)')
aff_level_unique_device_df = data.groupby('affiliate_id')['google_aid','ios_ifa'].nunique()
print (aff_level_unique_device_df)


# In[7]:


aff_level_unique_device_df.columns


# In[8]:


aff_level_unique_device_df= aff_level_unique_device_df.reset_index()


# In[9]:


aff_level_unique_device_df.head()


# ## Question 1(b)
# Calculate how many valid google_aid & ios_ifa exist in the dataset.

# In[10]:


data['google_aid'].value_counts()


# In[11]:


data['google_aid'].isnull().values.any()


# ## Method for checking Valid IDs

# In[12]:


def valid_google_aid(device_id):
    if(device_id != device_id):
        return False
    regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
    match = regex.match(device_id)
    return bool(match)


def valid_ios_ifa(device_id):
    if(device_id != device_id):
        return False
    regex = re.compile('^[A-F0-9]{8}-?[A-F0-9]{4}-?4[A-F0-9]{3}-?[89AB][A-F0-9]{3}-?[A-F0-9]{12}\Z', re.I)
    match = regex.match(device_id)
    return bool(match)


# In[13]:


# Checking if google_aid has NAN or Null
data['google_aid'].isnull().values.any()


# In[14]:


# Checking if ios_ifa has NAN or Null
data['ios_ifa'].isnull().values.any()


# In[15]:


data['valid_google_aid'] = data['google_aid'].apply(valid_google_aid)


# In[16]:


data['valid_ios_ifa'] = data['ios_ifa'].apply(valid_ios_ifa)


# In[17]:


data.head()


# ## Valid IOS_IFA

# In[18]:


data[data['valid_ios_ifa']==True].shape[0]


# ## Valid Google AID

# In[19]:


data[data['valid_google_aid']==True].shape[0]


# ## Valid Device ID at affiliate id level

# In[20]:


aff_level_unique_valid_device_df = data.groupby('affiliate_id')['valid_google_aid','valid_ios_ifa'].sum()
aff_level_unique_valid_device_df


# ## Question 2(a)
# Plot a histogram from the data obtained from exercise 1.a)

# In[21]:


aff_level_unique_device_df.head()


# In[22]:


aff_level_unique_device_df.plot(x='affiliate_id', y=['google_aid','ios_ifa'], kind='bar', legend=False)

# Scaling this because some values are very small 
plt.yscale("log")
plt.show()


# ## Question 2(b)
# 2.2) Plot a histogram of the no. of clicks v/s affiliate_id in the dataset.

# In[23]:


data.head(2)


# In[24]:


affiliate_vise_clicks = data[['affiliate_id']].groupby('affiliate_id').size().rename('Clicks').reset_index()


# In[25]:


affiliate_vise_clicks.columns


# In[26]:


print('Answer 2(b)')

affiliate_vise_clicks.plot(x='affiliate_id', y=['Clicks'], kind='bar', legend=False)

# Scaling this because some values are very small 
plt.yscale("log")
plt.show()


# In[ ]:




