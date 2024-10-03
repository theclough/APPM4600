import time
import math
import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm

def driver():

    # problem setup
    x0 = np.array([1,0])
    tol = 10**(-10)
    Nmax = 100
    opt = 1

    # calculations and time
    t = time.time()
    for j in range(50):
        [xstar,ier,its] = SlackyNewton(x0,tol,Nmax, opt)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier)
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)
    print('F(x[]) = ', evalF(xstar,opt))
    print('--------------------------------------------')

    x0 = np.array([0.1, 0.1, -0.1])
    opt = 2
    t = time.time()
    for j in range(50):
        [xstar,ier,its] = SlackyNewton(x0,tol,Nmax, opt)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier)
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)
    print('F(x[]) = ', evalF(xstar,opt))

def evalF(x, opt):

    if opt == 1:
        F = np.zeros(2)
        F[0] = 4*x[0]**2 + x[1]**2 - 4
        F[1] = x[0] + x[1] - math.sin(x[0]-x[1])
    else:
        F = np.zeros(3)
        F[0] = 3*x[0]-math.cos(x[1]*x[2])-1/2
        F[1] = x[0]-81*(x[1]+0.1)**2+math.sin(x[2])+1.06
        F[2] = np.exp(-x[0]*x[1])+20*x[2]+(10*math.pi-3)/3
    
    return F

def evalJ(x,opt):

    if opt == 1:
        J = np.array([[8*x[0],2.*x[1]],[1-math.cos(x[0]-x[1]),1+math.cos(x[0]-x[1])]])
    else:
        J = np.array([[3.0, x[2]*math.sin(x[1]*x[2]), x[1]*math.sin(x[1]*x[2])],
        [2.*x[0], -162.*(x[1]+0.1), math.cos(x[2])],
        [-x[1]*np.exp(-x[0]*x[1]), -x[0]*np.exp(-x[0]*x[1]), 20]])
    
    return J

def SlackyNewton(x0,tol,Nmax,opt):
# Slacker Newton = use the inverse of the Jacobian for initial guess & recompute to not converge fast enough
#       - check condition is if norm(successive iterations) > 2*norm(initial)
# inputs: x0 = initial guess, tol = tolerance, Nmax = max its
# Outputs: xstar= approx root, ier = error message, its = num its
    J = evalJ(x0,opt)
    Jinv = inv(J)
    
    for its in range(Nmax):
        F = evalF(x0,opt)
        if (norm(F) == 0):
        # inital guess was solution
            xstar = x1
            ier = 0 
            return[xstar, ier,its]
        x1 = x0 - Jinv.dot(F)
        if its == 0:
        # get diff to recompute Jacobian
            diffx0 = abs(x1[0]-x0[0])
            diffy0 = abs(x1[1]-x0[1])
        if (abs(x1[0]-x0[0]) < tol) and (abs(x1[1]-x0[1]) < tol):
            xstar = x1
            ier =0
            return[xstar, ier,its]
        if (abs(x1[0]-x0[0]) > diffx0) or (abs(x1[1]-x0[0]) > diffy0):
        # recompute Jacobian
            J = evalJ(x0,opt)
            Jinv = inv(J)
        x0 = x1
        
    xstar = x1
    ier = 1
    
    return[xstar,ier,its]

driver()