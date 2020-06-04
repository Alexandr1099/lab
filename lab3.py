#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print (root.data) 
        inorder(root.right) 
  
def insert(node, data): 
    if node is None: 
        return Node(data) 
  
    if data < node.data: 
        node.left = insert(node.left, data) 
    else: 
        node.right = insert(node.right, data) 
  
    return node 
  
def minValueNode(node): 
    current = node 
  
    while(current.left is not None): 
        current = current.left  
  
    return current  
  
def deleteNode(root, data): 
    if root is None: 
        return root  

    if data < root.data: 
        root.left = deleteNode(root.left, data) 
    elif(data > root.data): 
        root.right = deleteNode(root.right, data) 
  
    else:        
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = minValueNode(root.right) 

        root.data = temp.data 

        root.right = deleteNode(root.right , temp.data) 
  
    return root  

def getLevel(node, data, level=1): 
    if (node == None): 
        return 0
  
    if (node.data == data) : 
        return level  
  
    downlevel = getLevel(node.left, data, level + 1)  
    if (downlevel != 0) : 
        return downlevel  
  
    downlevel = getLevel(node.right, data, level + 1)  
    return downlevel  
  

def findval(root, lkpval):
    if lkpval < root.data:
        if root.left is None:
            return None
        return findval(root.left, lkpval)
    elif lkpval > root.data:
        if root.right is None:
            return None
        return findval(root.right, lkpval)
    else:
        return root.data

##########################__Work Area__##################################
  
#""" Let us create following BST 
#              5 
#           /     \ 
#           3      7 
#         /  \    /  \ 
#        2    4  6   8 """


root = None
root = insert(root, 5) 
root = insert(root, 3) 
root = insert(root, 2) 
root = insert(root, 4) 
root = insert(root, 7) 
root = insert(root, 6) 
root = insert(root, 8) 

print ("\nInorder traversal of the given tree")
inorder(root) 

print ("\nDelete 2")
root = deleteNode(root, 2) 
print ("Inorder traversal of the modified tree")
inorder(root) 

print ("\nDelete 3")
root = deleteNode(root, 3) 
print ("Inorder traversal of the modified tree")
inorder(root) 

print ("\nDelete 5")
root = deleteNode(root, 5) 
print ("Inorder traversal of the modified tree")


# In[7]:


inorder(root)
import random
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print (root.data) 
        inorder(root.right) 
  
def insert(node, data): 
    if node is None: 
        return Node(data) 
  
    if data < node.data: 
        node.left = insert(node.left, data) 
    else: 
        node.right = insert(node.right, data) 
  
    return node 
  
def minValueNode(node): 
    current = node 
  
    while(current.left is not None): 
        current = current.left  
  
    return current  
  
def deleteNode(root, data): 
    if root is None: 
        return root  

    if data < root.data: 
        root.left = deleteNode(root.left, data) 
    elif(data > root.data): 
        root.right = deleteNode(root.right, data) 
  
    else:        
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = minValueNode(root.right) 

        root.data = temp.data 

        root.right = deleteNode(root.right , temp.data) 
  
    return root  

def getLevel(node, data, level=1): 
    if (node == None): 
        return 0
  
    if (node.data == data) : 
        return level  
  
    downlevel = getLevel(node.left, data, level + 1)  
    if (downlevel != 0) : 
        return downlevel  
  
    downlevel = getLevel(node.right, data, level + 1)  
    return downlevel  
  

def findval(root, lkpval):
    if lkpval < root.data:
        if root.left is None:
            return None
        return findval(root.left, lkpval)
    elif lkpval > root.data:
        if root.right is None:
            return None
        return findval(root.right, lkpval)
    else:
        return root.data

##########################__Work Area__##################################
  
#""" Let us create following BST 
#              5 
#           /     \ 
#           3      7 
#         /  \    /  \ 
#        2    4  6   8 """


root = None
root = insert(root, 5) 
root = insert(root, 3)
root = insert(root, 2) 
root = insert(root, 4) 
root = insert(root, 7) 
root = insert(root, 6) 
root = insert(root, 8) 


""" LVL """
print ("Get Level of a node in a Binary Tree")
x = 7
level = getLevel(root, x) 
if (level) : 
    print("Level of", x, "is", level) 
else: 
    print(x, "is not present in tree")


# In[8]:


import random
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print (root.data) 
        inorder(root.right) 
  
def insert(node, data): 
    if node is None: 
        return Node(data) 
  
    if data < node.data: 
        node.left = insert(node.left, data) 
    else: 
        node.right = insert(node.right, data) 
  
    return node 
  
def minValueNode(node): 
    current = node 
  
    while(current.left is not None): 
        current = current.left  
  
    return current  
  
def deleteNode(root, data): 
    if root is None: 
        return root  

    if data < root.data: 
        root.left = deleteNode(root.left, data) 
    elif(data > root.data): 
        root.right = deleteNode(root.right, data) 
  
    else:        
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = minValueNode(root.right) 

        root.data = temp.data 

        root.right = deleteNode(root.right , temp.data) 
  
    return root  

def getLevel(node, data, level=1): 
    if (node == None): 
        return 0
  
    if (node.data == data) : 
        return level  
  
    downlevel = getLevel(node.left, data, level + 1)  
    if (downlevel != 0) : 
        return downlevel  
  
    downlevel = getLevel(node.right, data, level + 1)  
    return downlevel  
  

def findval(root, lkpval):
    if lkpval < root.data:
        if root.left is None:
            return None
        return findval(root.left, lkpval)
    elif lkpval > root.data:
        if root.right is None:
            return None
        return findval(root.right, lkpval)
    else:
        return root.data

""" 100 """
quantity = 5
arrInsertTimes = []
arrFindTimes = []

count = 100 + 1
print("--- ", count - 1, " ---")
items = random.sample(range(count), count-1)
for q in range(quantity) :
    print(q+1)

    root = None

    """Insert"""
    for item in items:
        startTime = time.time()

        root = insert(root, item)

        endTime = time.time()
    dis = endTime - startTime 
    arrInsertTimes.append(dis)

    """Find"""
    print ("\nFind value of the tree")
    x = random.randrange(count-1)
    startTime = time.time()
    val = findval(root, x)
    endTime = time.time()

    if(val) : 
        print(val, "is found")
    else :
        print("Value (", x,") not found")
    dis = endTime - startTime
    print("Find func time execution =", dis)

    arrFindTimes.append(dis)

fig = plt.figure()
fig.suptitle("Insert Times ", fontsize=20)
plt.plot(range(1, quantity+1), arrInsertTimes)
plt.show()

fig = plt.figure()
fig.suptitle("Find Times ", fontsize=20)
plt.plot(range(1, quantity+1), arrFindTimes)
plt.show()


# In[ ]:




