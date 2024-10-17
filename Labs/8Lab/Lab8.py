# Lab 8

import numpy as np
import matplotlib.pyplot as plt
import interp
from demo_linspline import demoDriver
from demo_cubicspline import demoDriver3
import monomial_interp

def driver():

    Q3_2()

    return

def gimmeNodes(n,opt=0):
# gives n+1 nodes
    
    h = 2/(n-1)
    nodes = np.zeros(n+1)
    for ii in range(n+1):
        nodes[ii] = -1 + (ii-1)/h
    return nodes

def Exercises():
# repeated experiments from Lab 7
# for linear and cubic splines

    f = lambda x: 1.0/(1+(10*x)**2)
    Neval = 1000
    a,b = (-1,1)
    xvals = np.linspace(a,b,Neval)
    demoDriver(xvals,Neval,a,b,f,8)
    # for ii in range(2,11):
    #     demoDriver(xvals,Neval,a,b,f,ii)
    #     demoDriver3(f,a,b,ii,Neval)
    
Exercises()