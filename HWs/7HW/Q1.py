# HW7 / Lab7 repeat

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

np.set_printoptions(precision=10)

def driver():
# run the stuff

    vanderMonde()
    
    return

def testVandy(fVals,p_x,iPts):
# checks that p(xi) = f(xi) for all i

    print([p_x(iPt) for iPt in iPts])
    print(fVals)
    return


def vanderMonde():#(a,b,n,iPts,f):
# constructs interpolation polynomial, p(x), using
# VanderMonde matrix
# Inputs:
#     (a,b)   : interval
#     n       : number of iterpolation points
#     iPts    : interpolation points
#     f       : actual function
# Outputs:
#     pVals   : p(x) values

# inital data
    n = 3
    a,b = (-1,1)
    nEval = 1001
    xVals = np.linspace(a,b,nEval)
    f = lambda x: 1.0/(1.0 + (10.0*x)**2)
    iPts = np.linspace(a,b,n)
    
# make y vector
    fVals = [f(iPt) for iPt in iPts]

# construct V
    V = np.ones((n,n))
    for ii in range(n):
        for jj in range(n-1):
            V[ii,jj] = iPts[ii]**(n-1-jj)            

# invert V and solve for c
# also define p(x)
    cVals = la.inv(V) @ fVals
    p = lambda x: sum(c*(x**(n-1-ii)) for c,ii in zip(cVals,range(n)))
    #testVandy(fVals,p,iPts)

# use c to determine p(x) values

    pVals = [p(x) for x in xVals]

# plot results

    plt.plot(iPts,f(iPts),'bo')
    plt.plot(xVals,f(xVals),'g-',label='exact')
    plt.plot(xVals,p(xVals),'b-',label='p(x)')
    plt.title('n = ' + str(n))
    plt.legend()
    plt.show()

driver()