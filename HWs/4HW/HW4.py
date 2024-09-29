# HW 4

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from bisection import bisection
from newtonsMethod import newtonsMethod

def printResults(astar, ier, count, Qnum, pnum, lastDash=1):
# prints results for bisection method
    if Qnum != 0:
        print(93*' ',Qnum)
    print(93*' ','---------------------------------------------------------')
    if pnum != 0:
        print(93*' ',pnum)
    print(93*' ','the error message is: ',ier)
    print(93*' ','the approximate root is: ', astar)
    print(93*' ','it took ', count, ' iterations')
    if lastDash != 0:
        print(93*' ','---------------------------------------------------------')

def Q1():
# Question 1

# (a)

    Ti = 20; Ts = -15;
    # Ti = initial soil temp, Ts = constant cold temp
    at = 0.138*5.184
    # at = (thermal conductivity)*(60 days in seconds)

    b = 0.1
    while(erf(b/(2*np.sqrt(at))) < 0.43):
        b += 0.1
    #print(erf(b/(2*np.sqrt(at))))
    #print(b)
    # find endpoint s.t. f(b) > 0
    # b = 0.7

    f = lambda x: 35*erf(x/(2*np.sqrt(at))) - 15
    xvals = np.linspace(0,0.7,100)
    plt.plot(f(xvals),-xvals,'b--')
    plt.ylabel('meters (relative to ground)')
    plt.xlabel('Temp (after 60 days)')
    plt.title('Q1 - (a)')
    
# (b)

    tol = 10**(-13)
    
    a = 0; b = 0.7
    [astar, ier, count] = bisection(f,a,b,tol)
    printResults(astar, ier, count, 'Q1,b : Bisection Method',0)

# (c) 

    p0 = 0.01
    fPrime = lambda x: 70/np.pi*np.exp(-(x/(2*np.sqrt(at))**2))
    [astar, ier, count] = newtonsMethod(f,fPrime,p0,tol)
    printResults(astar, ier, count, 'Q1,c : Newtons Method', 'initial guess = 0.01',0)
    p0 = 0.7
    [astar, ier, count] = newtonsMethod(f,fPrime,p0,tol)
    printResults(astar, ier, count, 0,'initial guess = 0.7')

    plt.show()

Q1()