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


# In[1]:


import matplotlib.pyplot as plt
x = [1,2,6,18]
y = [3,10,20,30]
plt.plot(x,y,'r:o')
plt.show()




# In[2]:


import matplotlib.pyplot as plt
x = [1,2,3,4]
y=[1,4,9,16]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.bar(x,y)
plt.show()


# In[3]:


import matplotlib.pyplot as plt
men = [22,30,35,35,26]
women = [25,32,30,35,29]
x = [1,2,3,4,5]
plt.bar(x,men,width=0.4,label="Men")
plt.bar([i+0.4 for i in x],women,width=0.4,label="Women")
plt.xlabel("Group")
plt.ylabel("Scores")
plt.legend()
plt.show()


# In[10]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[3,10,12,20,1]
plt.plot(x,y1,label="Line 1")
plt.plot(x,y2,label="Line 2")
plt.legend()
plt.show()


# In[11]:


import matplotlib.pyplot as plt

language=["Java","Python","PHP","JavaScript","C#","C++"]
popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.pie(popularity,labels=language,autopct="%1.1f%%")

plt.subplot(1,3,2)
plt.scatter(language,popularity)
plt.xticks(rotation=45)

plt.subplot(1,3,3)
plt.barh(language,popularity)
plt.grid()

plt.tight_layout()
plt.show()


# In[ ]:




