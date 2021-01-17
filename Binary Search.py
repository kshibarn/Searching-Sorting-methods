# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:58:23 2020

@author: user
"""

n=int(input("Enter no. of elements"))
a=[int(input())for i in range(n)]
l=0
u=n-1
p=-1
e=int(input("Enter the search element"))
while(l<=u):
    m=(l+u)//2
    if a[m]==e:
        p=m+1
        break
    else:
        if a[m]>e:
            u=m-1
        else:
            l=m+1
if p==-1:
    print("Element not found")
else:
    print("Element found at position",p)
