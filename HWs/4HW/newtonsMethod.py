# Newtons Method

import numpy as np

def newtonsMethod(g,gPrime, p0,tol,Nmax=300):
# Inputs:
#     - g, gPrime : g(x), g'(x) that seek root of
#     - p0 : initial guess (must be close to root)
#     - tol, Nmax : tolerance, max # of iterations
# Outputs:
#     -pstar : approximate root
#     -ier : 0 = good, 1 = bad inital guess, 2 = g'(p) was 0
#     -count : iterations to find root


#Check if guess is root & g'(p0) != 0
    if g(p0) == 0:
        return [p0, 0, 0]
    gPp = gPrime(p0)
    if gPp == 0:
        return [p0, 2, 0]

# Iterate through
    gp = g(p0)
    pstar = p0 - gp/gPp
    count = 1
    while(abs(gp-g(pstar))/abs(gp) > tol):
        count += 1
        if count > Nmax:
        # bad initial guess : ier = 1
            return [p0, 1, count]
        p0 = pstar
        gp = g(p0)
        if gp == 0:
        # found root : ier = 0
            return [p0, 0, count]
        gPp = gPrime(p0)
        if gPp == 0:
        # g'(p) = 0 : ier = 2
            return [p0, 2, count]
        pstar = p0 - gp/gPp

# return stuff if success
    return [pstar, 0, count]