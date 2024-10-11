# 2 methods
# 1) Broyden (sherman-morrison)
# 2) Lazy Newton

import math
import numpy as np
import numpy.linalg as la

def evalF(x0):
# evaluates F from Q2

    x,y,z = x0
    return np.array([x + np.cos(x*y*z) - 1,
                  (1-x)**(1/4) + y + 0.05*z**2 - 0.15*z -1,
                  -x**2 - 0.1*y**2 + 0.01*y + z - 1])

def evalJ(x,y,z):
# evalutes Jacobian from Q2

    return np.array
    

def newtons(J,tol,x0,Nmax=100):
# implements newton's method
# returns [ier, xstar, count]

    n = len(x0)
    x1 = np.zeros(n)
    for ii in range(Nmax):
        J1 = [[J[ii,jj](x0[0],x0[1],x0[2]) for jj in range(n)] for ii in range(n)]
        J2 = la.inv(J1) @ evalF(x0)
        x1 = x0 - np.transpose(J2)
        for jj in range(n):
        # stopping conditon:
        #   relative errors of each term below tolerance
            if abs(x1[jj]-x0[jj]) < tol:
                quit = 1
            else:
                quit = 0
        if quit:
            return [0, x1, ii]
        x0 = x1

    return [1,x0,Nmax]
                

def evalNormSqrd(x0,x1):
# calculates (x1 - x0)^2 in 2 norm

    sum = 0
    for ii in range(len(x0)):
        sum += (x1[ii] - x0[ii])**2

    return math.sqrt(sum)

def approxJacobian(J,F,x0,x1):
# calculates A = approx Jacobian
#  
#   = J(x0) + [F(x1)-F(x0)-J(x0)](x1-x0)'/||x1-x0||_2^2

    n = len(x0)
    result = np.zeros([n,n])
    for ii in range(n):
        return



def Q2():
# Question 2
#   3 Methods

    # 1) Newtons

    # define Jacobian
    dfdx1 = lambda x,y,z: 1 - y*z*np.sin(x*y*z)
    dfdx2 = lambda x,y,z: -x*z*np.sin(x*y*z)
    dfdx3 = lambda x,y,z: -x*y*np.sin(x*y*z)
    dgdx1 = lambda x,y,z: -0.25*(1-x)**(-0.25)
    dgdx2 = lambda x,y,z: 1
    dgdx3 = lambda x,y,z: 0.10*z - 15
    dhdx1 = lambda x,y,z: -2*x
    dhdx2 = lambda x,y,z: -0.2*y + 0.01
    dhdx3 = lambda x,y,z: 1
    J = np.array([[dfdx1, dfdx2, dfdx3],
                  [dgdx1, dgdx2, dgdx3],
                  [dhdx1, dhdx2, dhdx3]])

    x0 = np.array([0,0.1,1])
    tol = 10**(-6)
    [ier, xstar, count] = newtons(J,tol,x0)

    print('HW 6 - Q1')
    print('-------------------------------')
    print('Part 1 : Newtons')
    print('- - - - - - - - - - - - - - - -')
    print('the initial guess was: ', x0)
    print('the error message reads: ', ier)
    print('the approximate root is: ', xstar)
    print('the number of iterations was: ', count)
    print(evalF(xstar))
    
    x0 = np.array([0.1,0.2,1.1])
    tol = 10**(-6)
    [ier, xstar, count] = newtons(J,tol,x0)

    print('- - - - - - - - - - - - - - - -')
    print('perturb by 0.1 for each root:')
    print('the initial guess was: ', x0)
    print('the error message reads: ', ier)
    print('the approximate root is: ', xstar)
    print('the number of iterations was: ', count)
    print(evalF(xstar))

    # 2) Steepest Descent

Q2()