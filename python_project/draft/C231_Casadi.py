#!/usr/bin/python3

from casadi import *
import numpy as np
import casadi

a = np.array([[1,1], [2,2]])
b = np.array([[1,1], [1,1]])
print(a@b)
print(a*b)
print("-----------")
print(casadi.dot(a,b))