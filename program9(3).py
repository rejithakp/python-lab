#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
op=input("Enter operator +,-,*,/,%,^")
if(op=="+"):
    print("sum is:",a+b)
elif(op=="-"):
    print("difference is:",a-b)
elif(op=="*"):
    print("product is:",a*b)
elif(op=="/"):
    print("quotient is:",a/b)
elif(op=="%"):
    print("remainder is:",a%b)
elif(op=="^"):
    print("power is:",a**b)
else:
    print("Not recognised operator")
    


# In[ ]:




