# Lab 3, Tyler Clough
import numpy as np
import matplotlib.pyplot as plt
from fixedpt_example import fixedpt
from bisection_example import bisection

def print_results(f,astar,ier,name='root'):
# prints results of bisection/fixedpt algorithms

    print('the approximate ',name,' is',astar)
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
        [astar,ier] = bisection(f,int[0],int[1],tol)
        print_results(f,astar,ier)
    # loops over each interval and prints results

def Q2():
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
        [astar,ier] = bisection(func,int[0],int[1],tol)
        print_results(func,astar,ier)
    # loops over each interval and prints results
    [astar,ier] = bisection(f_c,0.5,3*np.pi/4,tol)
    print_results(f_c,astar,ier)
    # trys sin() again with diffferent interval

def Q3():
# code for Question 4-3

    f_a = lambda x: x*(1+(7-x**5)/(x**2))**3
    f_b = lambda x: x-(x**5-7)/(x**2)
    f_c = lambda x: x-(x**5-7)/(5*x**4)
    f_d = lambda x: x-(x**5-7)/12
    # stuff given by problem statement

    fp = 7**(1/5)
    print(f_a(fp))
    print(f_b(fp))
    print(f_c(fp))
    print(f_d(fp))
    print(fp)
    # verify fp is fixed point for all funcs

    tol = 10**(-10)
    # tolerance
    x0 = 1
    # initial guess
    xvals = np.linspace(0.75,1.25,100)
    # for plotting functions
    for func in [f_a,f_b,f_c,f_d]:
        #plt.plot(xvals,func(xvals),'bo')
        #plt.show()
        try:
            [astar, ier]=fixedpt(func,x0,tol,50)
            print_results(func,astar,ier,'fixed point')
        except:
            print('error')

Q3()