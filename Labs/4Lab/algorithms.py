# algorithms that have made so far:
# -fixed point
# -Aitken's Method
# -compute order

# import libraries
import numpy as np

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    results = [-1]
    count = 0
    while (count <Nmax):
        count = count +1 
        try:
            x1 = f(x0)
            results += [x1]
            if (abs(x1-x0) <tol):
                xstar = x1
                ier = 0
                return [xstar,ier,results[1::]]
            x0 = x1
        except:
            print('error: ',x0)
            break
    xstar = x1
    ier = 1
    return [xstar, ier,results[1::]]

def aitkensMethod(f,x0,tol,Nmax):
# applies Aitken's Method to Fixed Point Iteration 
    results = [-1]
# Get first 2 values for Aitken's (have 3 with x0)
# via normal fixed point iteration
    x1 = f(x0)
    results += [x1]
    if (abs(x1-x0) <tol):
        xstar = x1
        ier = 0
        return [xstar,ier,results[1::]]
    x2 = f(x1)
    results += [x2]
    if (abs(x2-x1) <tol):
        xstar = x2
        ier = 0
        return [xstar,ier,results[1::]]
# Apply Aitken's Method
    count = 3
    while (count < Nmax):
        count = count +1 
        try:
            x3 = f(x2)
            # (x1**2 - x0*x2)/(2*x1 - x0 - x2)
            # p = (p_{n+1}^2-p_n*p_{n+2})/(2*p_{n+1}-p_n-p_{n+2})
            results += [x3]
            if (abs(x3-x2) <tol):
                xstar = x3
                ier = 0
                return [xstar,ier,results[1::]]
            x0 = x1
            x1 = x2
            x2 = x3
        except:
            print('error: ',x0)
            break
    xstar = x3
    ier = 1
    return [xstar, ier,results[1::]]

def compute_order(pStar,pVec):
#    Inputs:
#        -p = fixed point
#        -pVec = vector of all approximations from fixed point iteration
#    Output:
#        -a = alpha = order of convergence
#        -l = lambda = rate
    p = pStar*np.ones(len(pVec)-1)
    diff1 = np.abs(pVec[1::]-p)
    # top of order ratio
    diff2 = np.abs(pVec[0:-1]-p)
    # bottom of order ratio
    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)
    # finds coeffs for log(p_{n+1}-p) = log(l) + a*log(p_n-p)

    print('log(|p_{n+t}-p|) = log(l) + a*log(p_n-p)')
    print('from ^ the order of the equation is: ')
    print('lambda = ', str(np.exp(fit[1])))
    print('alpha = ', str(fit[0]))
    # print results

    return [fit, diff1, diff2]






