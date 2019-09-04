
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[10]:


x = np.arange(0,4*np.pi,0.2)   # start,stop,step  
sine = np.sin(x)


# In[15]:


plt.plot(x,sine)
plt.show()


# In[16]:


cos = np.cos(x)
plt.plot(x,cos)


# In[22]:


plt.plot(x,sine,x,cos)
plt.xlabel('x values') 
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos')
plt.legend(['sin(x)', 'cos(x)'])       
plt.show()

