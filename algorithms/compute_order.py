# Compute Order

import numpy as np

def compute_order(pStar,pVec):
#    Inputs:
#        -p = fixed point
#        -pVec = vector of all approximations from fixed point iteration
#    Output:
#        -a = alpha = order of convergence
#        -l = lambda = rate
    l = len(pVec)
    diff1 = [np.abs(pVec[ii]-pStar) for ii in range(1,l)]
    # |p_{n+1} - p|
    diff2 = [np.abs(pVec[ii]-pStar) for ii in range(l-1)]
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