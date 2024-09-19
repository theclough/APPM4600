# for Lab 4
# import libraries
import numpy as np

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
    if (abs(x2-x1) <tol):
        xstar = x2
        ier = 0
        return [xstar,ier,results[1::]]
# Apply Aitken's Method
    count = 3
    while (count < Nmax):
        count = count +1 
        try:
            x3 = (x1**2 - x0*x2)/(2*x1 - x0 - x2)
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