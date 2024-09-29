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
    d = a + 0.5*(b-a)
    # improvement from textbook
    #   -add small correction to a rather than 
    #       computing (a+b)/2 to avoid roundoff error
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
        if (np.sign(fa)*np.sign(fb) == -1):
        # root in interval (a,d)
        # uses np.sign() instead of fa*fb to avoid possible under/overflow
            b = d
        else:
        # root in interval (d,b)
            a = d
            fa = fd
        d = a + 0.5*(b-a)
        count = count +1
      
    astar = d
    ier = 0
    return [astar, ier, count]             