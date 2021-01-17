# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:04:44 2020

@author: user
"""

n=int(input("Enter the no. of elements"))
a=[int(input())for i in range(n)]
m=int(input("Enter required element"))
f=0
for i in a:
    if i==m:
        f=1
        break
    if f==0:
        print("Element not found")
    else:
        print("Element found at position",a.index(i)+1)