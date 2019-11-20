import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4*np.pi,0.2)   # start,stop,step  
sine = np.sin(x)


plt.plot(x,sine)
plt.show()



cos = np.cos(x)
plt.plot(x,cos)

######### Adding tan function #########
tan = np.tan(x)
tan[:-1][np.diff(tan) < 0] = np.nan # to remove the asymptotes
# by default the sine and cosine graphs are between y ranges -1 and 1
# this is to prevent the y axis from increasing 
plt.ylim(-1,1)
# In[22]:

# added tan to plot, title and legend
plt.plot(x,sine,x,cos, x, tan)
plt.xlabel('x values') 
plt.ylabel('sin(x), cos(x) and tan(x)')
plt.title('Plot of sin , cos and tan')
plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])       
plt.show()

