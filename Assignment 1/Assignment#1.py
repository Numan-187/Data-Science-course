#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("Twinkle,Twinkle,little star,\n\tHow I wondee what you are!\n\t\tUp above the world so hight,\n\t\tLike a daimond in the sky,\nTwinkle,Twinkle,little star,\n\tHow I wondee what you are")


# In[24]:


import sys
print("Python version")
print (sys.version)


# In[12]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[15]:


r=int(input("Enter the Radius of the Circle: "))
area = 3.14*r*r
print(f"Area of the circle={area}")


# In[19]:


f_name=input("Enter the first name:")
l_name=input("Enter the last name:")
name=f_name+l_name
print(f"User full Name:{name}")
print(f"User full name in reverse order:{name[::-1]}")


# In[23]:


a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
sum=a+b
print("Sum=",sum)


# In[ ]:




