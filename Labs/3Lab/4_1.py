# Lab 3, Tyler Clough
import numpy as np
from bisection_example import bisection

def print_bisection(f,a,b,tol):
# prints results of bisection method

    print('------------------------')
    [astar,ier] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))

def Q1():
# code for Question 4-1
    
    f = lambda x: x**2*(x-1)
    a_interval = [0.5,2]
    b_interval = [-1,0.5]
    c_interval = [-1,2]
    # stuff given by problem statement
    tol = 10**(-5)
    # chose tolerance so it doesn't break my Chromebook
    
    for int in [a_interval,b_interval,c_interval]:
        print_bisection(f,int[0],int[1],tol)
    # loops over each interval and prints results

def Q5():
# code for Question 4-2

    tol = 10**(-5)
    f_a = lambda x: (x-1)*(x-3)*(x-5)
    f_b = lambda x: (x-1)**2*(x-3)
    f_c = lambda x: np.sin(x)
    a_interval = [0,2.4]
    b_interval = [0,2]
    c_interval = [0,0.1]
    # stuff given by problem statement

    for func,int in zip([f_a,f_b,f_c],[a_interval,b_interval,c_interval]):
        print_bisection(func,int[0],int[1],tol)
    # loops over each interval and prints results
    print_bisection(f_c,0.5,3*np.pi/4,tol)
    # trys sin() again with diffferent interval

Q5()
