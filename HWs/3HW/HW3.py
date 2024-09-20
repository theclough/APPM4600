# HW3, Tyler Clough

import numpy as np
from bisection import bisection
from computeOrder import compute_order

def printBisection(astar, ier, count):
# prints results for bisection method
    print('-----------------------')
    print("the error message is: ",ier)
    print("the approximate root is: ", astar)
    print("it took ", count, " iterations")
    print('-----------------------')

def Q1():
# Question 1, (c)
    f = lambda x: 2*x - np.sin(x) - 1
    tol = 10**(-9)
    a = -1; b = 2;
    # interval from (a)
    [astar, ier, count] = bisection(f,a,b,tol)
    printBisection(astar,ier, count) 

    return 0

def Q2():
# Question 2

    a = 4.82; b = 5.2; tol = 10**(-6)
    # given interval [a,b] and tolerance

    # (a)
    # using exact formula
    f_a = lambda x: (x-5)**9
    [astar, ier, count] = bisection(f_a,a,b,tol)
    print("Q2")
    print('-----------------------')
    print("(a)")
    printBisection(astar,ier, count)

    # (b)
    # using coeffs
    f_b = lambda x: x**9 - 45*x**8 + 900*x**7 \
    - 10500*x**6 + 78750*x**5 - 393750*x**4 \
    + 1312500*x**3 - 2812500*x**2 + 3515625*x \
    - 1953125
    [astar, ier, count] = bisection(f_b,a,b,tol)
    print("(b)")
    printBisection(astar,ier, count)

    return 0

def Q3():
# Question 3, (b)

    a = 1; b = 4; tol = 10**(-3);
    f = lambda x: x**3 + x - 4
    [astar, ier, count] = bisection(f,a,b,tol)
    printBisection(astar,ier, count)  

def Q4():
# Question 4

    # (a)
    pStar = 2
    pVec = np.zeros(100)
    pVec[0] = 3
    for ii in range(1,100):
        pVec[ii] = -16+6*pVec[ii-1] + 12/pVec[ii-1]
    #print('Q4 - (a)')
    compute_order(pStar,pVec)
    
    # (b)
    pStar = 3**(1/3)
    pVec = np.zeros(100)
    pVec[0] = 1.44
    # set initial value in correct interval
    for ii in range(1,100):
        pVec[ii] = 2*pVec[ii-1]/3 + (pVec[ii-1])**(-2)
    compute_order(pStar,pVec)
    
    # (c)
    pStar = 3
    pVec = np.zeros(100)
    #pVec[0] = 3
    # set initial value in correct interval
    for ii in range(1,100):
        pVec[ii] = 12/(1+pVec[ii-1])
    compute_order(pStar,pVec) 
    print('-----------------------')

Q4()