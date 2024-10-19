# HW7 / Lab7 repeat, Q2 & 3

import math
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

np.set_printoptions(precision=10)

def driver():
# run the stuff

    a,b = (-1,1)
    nEvals = 1001
    f = lambda x: 1.0/(1.0 + (10.0*x)**2)
    # for n in range(2,20):
    #     barry(f,a,b,n,nEvals)
    barry(f,a,b,51,nEvals)
    
    return

def weight(j,n,iPts):
# returns weight for given x
    w = 1
    for ii in range(n):
        if ii != j:
            w = w*(iPts[j]-iPts[ii])
    return 1.0/w

def cheby(n):
# returns array of Chebyshev nodes
    return np.array([math.cos((2.0*ii-1)*math.pi/(2*n)) for ii in range(1,n+1)])

def barry(f,a,b,n,nEvals):
# barycentric Lagrange interpolation

# initial data
    xVals = np.linspace(a,b,nEvals)
    iPts = cheby(n) #np.linspace(a,b,n)

# test function for if x = interpolation node
# 0 means x is node
    nodeCheck = lambda x: np.prod([(x-iPt) for iPt in iPts])

# construct p(x)
    pVals = np.zeros(nEvals)
    # initialize p(x) array
    idx = 0
    # index variable
    for x in xVals:
        if nodeCheck(x) == 0:
        # evaluating at interpolation node
            pVals[idx] = f(x)
        else:
        # calculate sums
            sum1,sum2 = 0,0
            for ii in range(n):
                w = weight(ii,n,iPts)
                sum1 += w/(x-iPts[ii])*f(iPts[ii])
                # numerator
                sum2 += w/(x-iPts[ii])
                # denominator
            pVals[idx] = sum1/sum2
        idx += 1

    plt.plot(iPts,f(iPts),'bo')
    plt.plot(xVals,f(xVals),'g-',label='exact')
    plt.plot(xVals,pVals,'b--',label='p(x)')
    # plt.xlim(-0.5,0.5)
    # plt.ylim(0,1.25)
    plt.title('n = ' + str(n))
    plt.legend()
    plt.savefig('barryN_'+str(n))
    plt.show()

    return

driver()