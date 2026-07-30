#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
a=np.array([[2,6],[3,5]])
b=np.array([[7,8],[9,1]])
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Matrix multiplication:",np.dot(a,b))
print("Transpose of a:",np.transpose(a))
print("Transpose of b:",np.transpose(b))



# In[15]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
U,S,VT=np.linalg.svd(a)
n_components=2


# In[18]:


import matplotlib.pyplot as plt
x=[3,5,6,8,9]
y=[1,2,3,4,5]
plt.plot(x,y)
plt.title("Hello World")
plt.xlabel("Petal")
plt.ylabel("Sepal")


# In[21]:


subject=["maths","science","history"]
mark=[10,20,30]
plt.bar(subject,mark)
plt.title("MCA")
plt.xlabel("Subject")
plt.ylabel("Mark")


# In[22]:


subject=["maths","science","history"]
mark=[10,20,30]
plt.scatter(subject,mark)
plt.title("MCA")
plt.xlabel("Subject")
plt.ylabel("Mark")


# In[27]:


subject=["maths","science","history"]
mark=[10,10,20,20,30,30,40,40]
plt.hist(mark)
plt.title("MCA")
plt.xlabel("Subject")
plt.ylabel("Mark")


# In[30]:


subject=["maths","science","history"]
mark=[10,10,20,20,30,30,40,40]
plt.plot(mark)
plt.legend(mark)
plt.title("MCA")
plt.xlabel("Subject")
plt.ylabel("Mark")


# In[31]:


subject=["maths","science","history"]
mark=[10,10,20,20,30,30,40,40]
plt.pie(mark)
plt.legend(mark)
plt.title("MCA")
plt.xlabel("Subject")
plt.ylabel("Mark")


# In[ ]:


a=[1,2,3,4]
b=[1,2,3,4]
c=[1,2,3,4]
x=np.array([0,1,2,3])
y=np.array([3,8,10])


