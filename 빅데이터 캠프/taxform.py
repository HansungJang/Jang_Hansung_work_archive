#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""calculate income tax""" 
income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

std_dec = 10000
add_dec = 3000 * dependents
tax = (0.2) * income - (std_dec + add_dec)

print("The income tax is $%.2f" % tax)

