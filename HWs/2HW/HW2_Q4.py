# HW 2 - Question 4
import random
import numpy as np
import matplotlib.pyplot as plt

def driver():
# driver function

    FourA()
    FourB()

def FourA():
# Q4-a
    t = np.arange(0,np.pi,np.pi/30)
    y = np.cos(t)   
# problem set up

    n = len(t)
    S = 0
    for ii in range(n):
        S += t[ii]*y[ii]
# calculates sum 

    print("the sum is: ",S)
# prints results

    return 0

def FourB():
# Q4-b

    theta = np.linspace(0,2*np.pi,100)
    R = 1.2; dr = 0.1; f = 15;
    x = lambda t: R*(1+dr*np.sin(f*t))*np.cos(t)
    y = lambda t: R*(1+dr*np.sin(f*t))*np.sin(t)
# given by problem statement

    plt.plot(theta,x(theta))
    plt.plot(theta,y(theta))
    plt.title('$1^{st}$ Plot')
    plt.show()
    plt.clf()
# 1st plot

    dr = 0.05
    for ii in range(10):
        R = ii
        f = 2+ii
        p = random.uniform(0,2)
        func = lambda t: R*(1+dr*np.sin(f*t+p))*np.cos(t)
        plt.plot(theta,func(theta))
    plt.title('$2^{nd}$ Plot')
    plt.show()
# 2nd plot
    
    return 0

driver()