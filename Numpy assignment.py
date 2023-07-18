#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Consider the below code to answer further questions:
import numpy as np

list = [ '1' , '2' , '3' , '4' , '5' ]

array_list = np.array(object = list)


# Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
# to print the data types of both the variables.

# In[13]:


list


# In[14]:


array_list


# In[15]:


type(list)


# In[16]:


type(array_list)


# Q2. Write a code to print the data type of each and every element of both the variables list_ and
# arra_list.

# In[17]:


list[0]


# In[18]:


type(list[0])


# In[24]:


for i in list:     #if we run for loop then we can also find or we can check by individual
    print(type(i))


# In[25]:


type(list[1])


# In[29]:


type(list[2]) #like wise


# In[30]:


array_list


# In[31]:


type(array_list[0])


# In[32]:


type(array_list[1])


# In[33]:


for i in array_list:
    print(type(i))


# Q3. Considering the following changes in the variable, array_list:
# array_list = np.array(object = list_, dtype = int)
# Will there be any difference in the data type of the elements present in both the variables, list_ and
# arra_list? If so then print the data types of each and every element present in both the variables, list_
# and arra_list.

# In[35]:


import numpy as np

list = [ '1' , '2' , '3' , '4' , '5' ]

array_list = np.array(object = list, dtype = int)


# In[36]:


list


# In[37]:


array_list


# In[38]:


type(list)


# In[39]:


type(array_list)


# In[41]:


for i in list:
    print(type(i))


# In[42]:


for i in array_list:
    print(type(i))


# In[43]:


#Consider the below code to answer further questions:
import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)


# In[44]:


num_list


# In[45]:


num_array


# In[46]:


type(num_list)


# In[47]:


type(num_array)


# Q4. Write a code to find the following characteristics of variable, num_array:
# (i) shape
# (ii) size

# In[50]:


num_array.shape


# In[51]:


num_array.size


# Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
# creation function.
# [Hint: The size of the array will be 9 and the shape will be (3,3).]

# In[52]:


list = [[0,0,0],
       [0,0,0],
       [0,0,0]]


# In[53]:


x = np.array(list)


# In[54]:


x


# In[55]:


x.size


# In[56]:


x.shape


# Q6. Create an identity matrix of shape (5,5) using numpy functions?
# [Hint: An identity matrix is a matrix containing 1 diagonally and other elements will be 0.]

# In[57]:


list = [[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0]]


# In[58]:


y = np.array(list)


# In[59]:


y


# In[60]:


y.shape


# In[ ]:




