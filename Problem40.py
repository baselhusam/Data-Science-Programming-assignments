#!/usr/bin/env python
# coding: utf-8

# In[3]:


def normBMI(weight, height):
    return weight/height**2


# In[4]:


def convertedBMI(weight, height):
    weight *= 0.4535919737
    height *= 0.0254
    return normBMI(weight,height)


# In[5]:


print(normBMI(73.8,1.8))


# In[6]:


print(convertedBMI(162.7011,70.8661))


# In[7]:


weight = float(input("Please enter your wight in kilograms: "))
height = float(input("Plase enter your height in meters: "))

print(normBMI(weight,height))


# In[8]:


weight_in_pounds = float(input("Please enter your weight in pounds: "))
height_in_inches = float(input("Plase enter your height in inches: "))

print(convertedBMI(weight_in_pounds,height_in_inches))


# In[ ]:




