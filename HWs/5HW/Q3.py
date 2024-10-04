# HW5, Q3
import time
import numpy as np
from numpy.linalg import inv, norm

def driver():

    tol = 10**(-10)
    Nmax = 100
    p0 = np.array([1.,1.,1.])
    t = time.time()
    for j in range(50):
        [pstar,ier,ct, pVec] = partB(p0,tol,Nmax)
    elapsed = time.time()-t
    for ii in range(5):
        print()
    print('Question 3 (b)')
    print('----------------------------------------------------------')
    print('the approximate root is', pstar)
    print('the error message reads:', ier)
    print('Number of iterations:', ct)
    print('it took on average', elapsed/50, '(s) over 50 trials')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    compute_order(pstar,pVec)
    print('-----------------------------------------------------------')
    for ii in range(5):
        print()

def compute_order(pStar,pVec):
#    Inputs:
#        -p = fixed point
#        -pVec = vector of all approximations from fixed point iteration
#    Output:
#        -a = alpha = order of convergence
#        -l = lambda = rate
    l = len(pVec)
    diff1 = [np.abs(pVec[ii][jj]-pStar[jj]) for ii in range(1,l) for jj in range(3)]
    # |p_{n+1} - p|
    diff2 = [np.abs(pVec[ii][jj]-pStar[jj]) for ii in range(l-1) for jj in range(3)]
    # |p_n - p|^a
    coeffs = np.polyfit(np.log(diff2),np.log(diff1),1)
    # finds coeffs for log(p_{n+1}-p) = a*log(p_n-p) + log(l)
    # i.e.                  y         = c1*x          +  c2

    print('log(|p_{n+1}-p|) = log(l) + a*log(p_n-p)')
    print('from ^ the order of the equation is: ')
    print('lambda = ', str(np.exp(coeffs[1])))
    print('alpha = ', str(coeffs[0]))
    # print results

    return [coeffs, diff1, diff2]

def evalD(x):
# evaluates d = f/(fx^2+fy^2+fz^2)

    x2 = x[0]**2
    y2 = x[1]**2
    z2 = x[2]**2

    return (x2 + 4*y2 + 4*z2 - 16)/(4*x2 + 64*y2 + 64*z2)

def partB(p0, tol, Nmax):

    p1 = np.zeros(3)
    iterations = [p0]
    for ii in range(Nmax):
        x0,y0,z0 = p0
        iterations += [[x0,y0,z0]]
        d = evalD(p0)
        p1[0] = x0 - 2*x0*d
        p1[1] = y0 - 8*y0*d
        p1[2] = z0 - 8*z0*d
        if (abs(p1[0]-x0) < tol) and (abs(p1[1]-y0) < tol) and (abs(p1[2]-z0) < tol):
            ier = 0
            pstar = p1
            return [pstar, ier, ii, iterations]
        p0 = p1
    
    ier = 1
    pstar = x0
    
    return [pstar, ier, Nmax, iterations]

driver()