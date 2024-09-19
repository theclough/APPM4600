# Lab 4, Tyler Clough
import algorithms
import numpy as np
import matplotlib.pyplot as plt

g = lambda x: (10/(x+4))**(1/2)
x0 = 1.5
tol = 10**(-10)
Nmax = 100
fixedP = 1.3652300134140976

def driver(opt):
# prints results for each question
    if opt == 2:
        Q2()
    elif opt == 3:
        Q3()
    Q4()

    return 0

def Q2():
# Question 2-2

    # (a)
    [pStar,ier,results] = algorithms.fixedpt(g,x0,tol,Nmax)
    # calculates fixed point
    print('the error message is: ',ier)
    print('the fixed points is: ',pStar)
    print('the number of iterations was: ',len(results))
    print('--------------------------')

    # (b)
    [fit, diff1, diff2] = algorithms.compute_order(fixedP,results)    

def Q3():
# Question 3
    [pStar,ier,results] = algorithms.aitkensMethod(g,x0,tol,Nmax)
    # implement Aiken's Method
    print('the error message is: ',ier)
    print('the fixed points is: ',pStar)
    print('the number of iterations was: ',len(results))
    print('--------------------------')
    [fit, diff1, diff2] = algorithms.compute_order(fixedP,results)   

def Q4():
# Question 4 - TBD

    return 0

driver(3)