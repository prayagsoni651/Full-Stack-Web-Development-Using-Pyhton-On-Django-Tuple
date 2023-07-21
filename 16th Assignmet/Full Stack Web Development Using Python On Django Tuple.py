#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a python script to store multiple items in a single variable ( Items are “Java”
# ,“Python”, “SQL”, “C” ) using tuple

hello = ("Java","Python","Sql","C")
tuple(hello)
print(hello)


# In[2]:


# 2. Write a python program to store only one item using tuple.

tuple1 = (20,)
print(tuple1,type(tuple1))


# In[14]:


# 3. Write a python program to reverse the tuple

tuple1 =(12,13,14,15,16,17)
tuple1[::-1]


# In[ ]:


# 4. Write a python program to Swap two tuples in Python.

tup1 = ('hello',12,24,36,48)
tup2 = (13,26,39,45,'bye')
tup1,tup2 = tup2,tup1
print(tup1,tup2)


# In[ ]:


# 5. Write a python program to check if all items in the tuple are the same.
tup1,tup2 = (34,35,36,37,38,"hello"),('hello','string',23,27,268)
if tup1==tup2:
    print("Tuple are the same")
else:
    print("tuple are not a same")


# In[ ]:


# 6. Write a python program to divide the tuple into four variables.
# tuple1=(100, 200, 300, 400)

tuple1 = (100,200,300,400)
divisior = eval(input("Enter a NUmber "))
result = tuple(value/divisior for value in tuple1)
print(result)


# In[ ]:


# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new
# tuple. tuple1=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)
new_tuple = tuple1[3:5]
print(new_tuple)


# In[5]:


# 8. Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
new_tuple = sorted(tuple1)
print(new_tuple)


# In[11]:


# 9. Write a python program to print the value 20 from given nested tuple
# tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

tuple1 = ("Python",[10,20,30],(2,4,16))
print("Accessing Elements =",tuple1[1][1])
print(tuple1)
          


# In[13]:


# 10. Write a python program to change the first item (22) of a list within the following tuple
# to 222.
# tuple1 = (11, [22, 33], 44, 55)



tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)
    
    


# In[ ]:





# In[ ]:




