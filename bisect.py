# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:00:09 2019

@author: ARCHIT
"""
from math import *

tolerance=1.0e-6
def f(x):
    f = x*x-5+sin(x)   #enter your function here
    return f

a=int(input("enter first guess "))
b=int(input("enter second guess "))
dx=abs(b-a)
while dx>tolerance:
    x=(a+b)/2.0
    if (f(a) * f(x)) < 0:
        b=x
    elif (f(a) * f(x)) == 0:
        break
    else:
        a=x
    dx = abs(b-a)

print("Found f ( x ) = 0 at x = %.8f +/− %0.8f " % ( x , tolerance)) 
