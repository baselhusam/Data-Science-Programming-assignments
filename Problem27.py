#!/usr/bin/env python
# coding: utf-8

# In[1]:


var_1 = 10
var_2 = 1
var_3 = 10
var_4 = 10
var_5 = '10'


# In[2]:


print(var_1)

# 27. A) 10


# In[4]:


print(var_2)

# 27. B) 1


# In[5]:


print("var_3")

# 27. C) var_3


# In[6]:


print((var_1+var_2)*var_3*var_4)

# 27. D) 1100


# In[7]:


print(((var_1+var_2)*var_3)/var_4)

# 27. E) 11.0


# In[8]:


print(var_1+(var_2*var_5)/var_4)

# 27. F) unsupported operand type(s) for /: 'str' and 'int'
#    Because (var_2 * var_5) will return a string value and in the next expression ((var_2*var_5)/var_4)
#    var_4 is and integer value so we CANT devide string value to integer which will conclude an error

