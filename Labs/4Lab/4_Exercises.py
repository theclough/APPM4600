# Lab 4, Tyler Clough
import numpy as np
import matplotlib.pyplot as plt
from fixedpt import fixedpt

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

    print('the order of the equation from,')
    print('log(|p_{n+t}-p|) = log(l) + a*log(p_n-p), is:')
    print('lambda = ', str(np.exp(fit[1])))
    print('alpha = ', str(fit[0]))
    # print results

    return [fit, diff1, diff2]

def Q2_2():
# Question 2-2

    # (a)
    g = lambda x: (10/(x+4))**(1/2)
    [pStar, ier, results] = fixedpt(g,1.5,10**(-10),100)
    # calculates fixed point
    print('the error message is: ',ier)
    print('the fixed points is: ',pStar)
    print('the number of iterations was: ',len(results))
    print('--------------------------')

    # (b)
    fixedP = 1.3652300134140976
    [fit, diff1, diff2] = compute_order(fixedP,results)
    print('--------------------------')

def Q3():
# Question 3

    # 3-1
    


Q2_2()