# HW3, Tyler Clough

import numpy as np
import matplotlib.pyplot as plt
from AlgorithmsHW3 import compute_order, fixedpt, bisection

def printBisection(astar, ier, count, opt):
# prints results for bisection method
    print('-----------------------')
    print(opt)
    print("the error message is: ",ier)
    print("the approximate root is: ", astar)
    print("it took ", count, " iterations")

def Q1():
# Question 1, (c)
    f = lambda x: 2*x - np.sin(x) - 1
    tol = 10**(-8)
    a = -1; b = 2;
    # interval from (a)
    [astar, ier, count] = bisection(f,a,b,tol)
    printBisection(astar,ier, count, 'Q1, (c)') 

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
    printBisection(astar,ier, count, '(a)')

    # (b)
    # using coeffs
    f_b = lambda x: x**9 - 45*x**8 + 900*x**7 \
    - 10500*x**6 + 78750*x**5 - 393750*x**4 \
    + 1312500*x**3 - 2812500*x**2 + 3515625*x \
    - 1953125
    [astar, ier, count] = bisection(f_b,a,b,tol)
    printBisection(astar,ier, count, '(b)')
    print('-----------------------')
    
    return 0

def Q3():
# Question 3, (b)

    a = 1; b = 4; tol = 10**(-3);
    f = lambda x: x**3 + x - 4
    [astar, ier, count] = bisection(f,a,b,tol)
    printBisection(astar,ier, count,'Q3')  

def Q4():
# Question 4

    print('Q4')

    # (a)
    pStar = 2
    pVec = np.zeros(100)
    pVec[0] = 3
    # set initial value in correct interval
    for ii in range(1,100):
        pVec[ii] = -16+6*pVec[ii-1] + 12/pVec[ii-1] 
    compute_order(pStar,pVec,'(a)')
    
    # (b)
    pStar = 3**(1/3)
    pVec = [1.2]
    # set initial value in correct interval
    count = 0
    while (pVec[count] != pStar):
    # had to use while loop bc converge so fast
    # that messing up polyfit() in compute_order
        pVec += [2*pVec[count]/3 + (pVec[count])**(-2)]
        count += 1
    compute_order(pStar,pVec[:-1],'(b)')
    
    # (c)
    pStar = 3
    pVec = np.zeros(100)
    pVec[0] = 3.5
    # set initial value in correct interval
    for ii in range(1,100):
        pVec[ii] = 12/(1+pVec[ii-1])
    compute_order(pStar,pVec,'(c)') 
    print('-----------------------')

def Q5():
# Question 5

    # (a)
    f = lambda x: x - 4*np.sin(2*x) - 3
    xVals = np.linspace(-5,10,200)
    zer0s = [0]
    for ii in range(1,200):
        # find 0s of function
        if f(xVals[ii])*f(xVals[ii-1]) < 0:
            zer0s += [(xVals[ii]+xVals[ii-1])/2]
    zer0s = zer0s[1::]
    plt.plot(xVals, f(xVals), 'r-')
    plt.plot(xVals, np.zeros(200),'k-')
    plt.plot(zer0s, np.zeros(len(zer0s)), 'go', label='zeros')
    plt.ylim(-7,7)
    plt.title('Q5 (a): $f(x) = x - 4\sin(2x) - 3$')
    plt.legend()
    plt.show()

    # (b)
    Xn = lambda x: -np.sin(2*x) + 5*x/4 - 3/4
    r0s = [-0.8, 0, 2, 3.5, 4.5];
    # initial guesses for each root
    tol = 0.5*10**(-10)
    # tolerance for 10 accurate digits
    print('Q5, (b)')
    print('-----------------------')
    for ii in range(len(r0s)):
        [xstar, ier, results] = fixedpt(Xn,r0s[ii],tol,100)
        print('root ', ii+1, ' is ~')
        print(xstar)
        [xstar, ier, results] = fixedpt(Xn,r0s[ii],10**(-20),100)
        print(xstar)
        print('-----------------------')

    return 0

Q1()