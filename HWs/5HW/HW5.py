# HW5
import math
import time
import numpy as np
from numpy.linalg import inv, norm

def driver():
# runs code for each Question
    Q1()
    
    return

def evalF(x):
# evaluates F = (f, g)

    F = np.zeros(2)
    F[0] = 3*x[0]**2 - x[1]**2
    F[1] = 3*x[0]*x[1]**2 - x[0]**3 - 1

    return F

def evalJinv_0(F_x):
# evaluates inverse Jacobian of F(x0), above

    Jinv = np.zeros(2)
    Jinv[0] = F_x[0]/6 + F_x[1]/16
    Jinv[1] = F_x[1]/6

    return Jinv

def evalJ(x):
# evaluates Jacobian of F(f,g)

    J = np.zeros([2,2])
    J[0,:] = [6*x[0], -2*x[1]]
    J[1,:] = [3*x[1]**2 - 3*x[0]**2, 6*x[0]*x[1]]

    return J

def y(x):
# evaluates y = J^(-1)*F(x)

    y = np.zeros(2)
    f = lambda x,y: 3*x**2 - y**2
    g = lambda x,y: 3*x*y**2 - x**3 - 1
    y[0] = (f(x[0],x[1]))/6 + (g(x[0],x[1]))/16
    y[1] = (g(x[0],x[1]))/16

    return y

def lazyNewton(x0,tol,Nmax):
# implemets Lazy Newton algorithm

    for ii in range(Nmax):
        F_x = evalF(x0)
        y = evalJinv_0(F_x)
        x1 = x0 - y
        if (abs(x1[0]-x0[0]) < tol and abs(x1[1]-x0[1]) < tol):
            ier = 0
            xstar = x1
            return [ier, xstar, ii]
        x0 = x1
    ier = 1
    xstar = x0

    return [ier, xstar, Nmax]

def newton(x0,tol,Nmax):
# implements Newton algorithm for linear systems

    for ii in range(Nmax):
        F_x = evalF(x0)
        Jinv_x = inv(evalJ(x0))
        x1 = x0 - np.dot(Jinv_x,F_x)
        if (abs(x1[0]-x0[0]) < tol and abs(x1[1]-x0[1]) < tol):
            ier = 0
            xstar = x1
            return [ier, xstar, ii]
        x0 = x1
    ier = 1
    xstar = x0

    return [ier, xstar, Nmax]
        

def Q1():
# Question 1

    # (a)
    tol = 10**(-10)
    Nmax = 100
    x0 = np.array([1,1])
    t = time.time()
    for j in range(50):
        [xstar,ier,ct] = lazyNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print('Question 1 (a) : Lazy Newton')
    print('------------------------------------------------')
    print('the approximate root is', xstar)
    print('the error message reads:', ier)
    print('Number of iterations:', ct)
    print('it took on average', elapsed/50, '(s) over 50 trials')
    print('------------------------------------------------')

    # (b)
    t = time.time()
    for j in range(50):
        [xstar,ier,ct] = newton(x0,tol,Nmax)
    elapsed = time.time()-t
    print('Question 1 (b) : Newton')
    print('------------------------------------------------')
    print('the approximate root is', xstar)
    print('the error message reads:', ier)
    print('number of iterations:', ct)
    print('it took on average', elapsed/50, '(s) over 50 trials')
    print('------------------------------------------------')
    
    return

driver()