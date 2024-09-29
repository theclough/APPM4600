# Aitken's Method

import numpy as np

def aitkensMethod(f,x0,tol,Nmax):
# applies Aitken's Method to Fixed Point Iteration 
    '''
    Inputs:
        -same as fixed point
    Outputs:
        -same as fixed point
    '''
    results = [-1]
# Get first 2 values for Aitken's (have 3 with x0)
# via normal fixed point iteration:
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
    x3 = (x1**2 - x0*x2)/(2*x1 - x0 - x2)
    # p = (p_{n+1}^2-p_n*p_{n+2})/(2*p_{n+1}-p_n-p_{n+2})
    pHat0 = x3 - (x1 - x3)**2/(x2 - 2*x1 + x3)
    # Aitken's D^2 Formula
    results += [pHat0]
    x0 = x1
    x1 = x2
    x2 = x3
# create {p_{\hat}} sequence:
    count = 4
    while (count < Nmax):
        count += 1 
        try:
            x3 = (x1**2 - x0*x2)/(2*x1 - x0 - x2)
            # p = (p_{n+1}^2-p_n*p_{n+2})/(2*p_{n+1}-p_n-p_{n+2})
            pHat1 = x3 - (x1 - x3)**2/(x2 - 2*x1 + x3)
            # Aitken's D^2 Formula
            results += [pHat1]
            if (abs(pHat1-pHat0) <tol):
                xstar = pHat1
                ier = 0
                return [xstar,ier,results[1::]]
            x0 = x1
            x1 = x2
            x2 = x3
            pHat0 = pHat1
        except:
            print('error: ',x0)
            break
    xstar = pHat1
    ier = 1
    return [xstar, ier,results[1::]]