#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import time
my_list = []
i = 0
n = 100
total_time = 0
while i < n:
    start = time.time()
    my_list.append(random.randint(1, 20))
    i = i + 1
    end = time.time()
    total_time = total_time + (end - start)
print("Кількість елементів масиву:",n )
print("Середній час виконання 1 операції:", total_time/n)
print("Сумарний час заповнення масиву:", total_time)
print("  ")
plt.plot(my_list)
total_time = 0
i = 0
while i < n:
    start = time.time()
    my_list.pop()
    i = i + 1
    end = time.time()
    total_time = total_time + (end - start)
print("Середній час виконання 1 операції:", total_time/n)
print("Сумарний час стирання елементыв масиву:", total_time)


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import time
my_list = []
i = 0
n = 100
while i < n:
    my_list.append(random.randint(1, 20))
    i = i + 1
#print(my_list)
print("Кількість елементів масиву:",n )
print("  ") 
start = time.time()
k = (n // 2)
my_list.pop(k)
my_list.pop(k-1)
end = time.time()
print("Час виконання 1 операції:", end - start)
plt.plot(my_list)
 


# In[6]:


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import time
my_list = []
i = 0
n = 100
while i < n:
    my_list.append(random.randint(1, 20))
    i = i + 1
start = time.time()
list_copy = copy.copy(my_list)
end = time.time()
print("Час виконання методу copy():",end - start)
plt.plot(list_copy)


# In[ ]:




