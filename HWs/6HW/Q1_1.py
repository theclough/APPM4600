import math
import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm

def driver():

    # problem setup
    tol = 10**(-10)
    Nmax = 100
    x0s = np.array([[1,1],[1,-1]])
    e1 = math.exp(1)
    J0 = np.array([[(2-2*e1)**(-1),-(1-e1)**(-1)],
                   [-e1/(2-2*e1), 2]])
    J1 = np.array([[(2+2*e1)**(-1),(1+e1)**(-1)],
                   [-e1/(2+2*e1), 2]])
    Jinvs = [J0, J1]

    # calculations and time
    print('HW 6 - Q1')
    print('------------------------------------------------------------------')
    print('Quasi Newton 1 : Lazy Newton')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    for x0,Jinv,i in zip(x0s,Jinvs,['(i)','(ii)']):
        [xstar,ier,its] = SlackyNewton(x0,tol,Jinv,Nmax)
        print('ICs ',i,':')
        print('the initial guess was: ', x0)
        print('the error message read: ', ier)
        print('the number of iterations was: ', its)
        print('the approximate root was: ', xstar)
        print('F(xstar) = ', evalF(xstar))
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    
    print('ICs (iii):')
    print('the initial guess was: ', [0,0])
    print('Lazy Newton fails because the Jacobian is singular')
    print('F(x0) = ', evalF([0,0]))
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

def evalF(x):

    F = np.zeros(2)
    F[0] = x[0]**2 + x[1]**2 - 4
    F[1] = math.exp(x[0]) + x[1] - 1
    
    return F

def evalJ(x0):

    x,y = x0
    return np.array([[2*x,2*y],[math.exp(x),1]])

def SlackyNewton(x0,tol,Jinv,Nmax):
# Slacker Newton = use the inverse of the Jacobian for initial guess & recompute to not converge fast enough
#       - check condition is if norm(successive iterations) > 2*norm(initial)
# inputs: x0 = initial guess, tol = tolerance, Nmax = max its
# Outputs: xstar= approx root, ier = error message, its = num its
    
    for its in range(Nmax):
        F = evalF(x0)
        if (norm(F) == 0):
        # inital guess was solution
            xstar = x1
            ier = 0 
            return[xstar, ier,its]
        x1 = x0 - Jinv.dot(F)
        if (abs(x1[0]-x0[0]) < tol) and (abs(x1[1]-x0[1]) < tol):
            xstar = x1
            ier =0
            return[xstar, ier,its]
        if (abs(x1[0]-x0[0]) > 1) or (abs(x1[1]-x0[0]) > 1):
        # recompute Jacobian
            J = evalJ(x0)
            Jinv = inv(J)
        x0 = x1
        
    xstar = x1
    ier = 1
    
    return[xstar,ier,its]