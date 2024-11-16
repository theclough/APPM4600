# HW 11
# Problem 1

import math
import numpy as np
import scipy.integrate as spicy

def printlines():
    print('-----------------------------------------------------')
    return

def eval_composite_trap(a,b,f,nPts):
# Inputs:
#     (a,b)   = interval
#     f       = function evaluating
#     nPts    = number of pts in interval
# Outputs:
#     approximate value of integral

    h = (b-a)/nPts
    quad = f(a)
    for ii in range(1,nPts):
        quad += 2.0*f(a+ii*h)
    quad += f(b)

    return 0.5*quad*h

def eval_composite_simpsons(a,b,f,nPts):
# Inputs:
#     (a,b)   = interval
#     f       = function evaluating
#     nPts    = number of pts in interval, must be even
# Outputs:
#     approximate value of integral

    if nPts%2 == 1:
        print('Error: Composite Simpsons requres even number of points')
        return 0

    h = (b-a)/nPts
    quad = f(a)
    for ii in range(1,nPts//2):
        quad += 2.*f(a + 2*ii*h)
    for ii in range(1,nPts//2+1):
        quad += 4.*f(a + (2*ii-1)*h)
    quad += f(b)

    return quad*h/3.