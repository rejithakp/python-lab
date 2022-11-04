#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cmath
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
d=(b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d)/(2*a))
sol2=(-b-cmath.sqrt(d)/(2*a))
print("The solution to quadratic equation are {} and {}".format(sol1,sol2))

