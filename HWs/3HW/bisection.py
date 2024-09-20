# import libraries
import numpy as np

def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#   Verify there is a root we can find in the interval:
    count = 0
    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, ier, count]

#   Verify end points are not a root: 
    if (fa == 0):
        astar = a
        ier =0
        return [astar, ier]
    if (fb ==0):
        astar = b
        ier = 0
        return [astar, ier, count]

#   Split interval in 1/2 and check for convergence to root
    d = 0.5*(a+b)
    while (abs(d-a) > tol):
    # put max on iterations
        fd = f(d)
        if (fd == 0):
        # found root
            astar = d
            ier = 0
            return [astar, ier, count]
        if count > 100:
            ier = 1
            astar = a
            return [astar, ier, count]
        if (fa*fd<0):
        # root in interval (a,d)
            b = d
        else:
        # root in interval (d,b)
            a = d
            fa = fd
        d = 0.5*(a+b)
        count = count +1
      
    astar = d
    ier = 0
    return [astar, ier, count]             