import numpy as np
import math
from numpy.linalg import inv
from lineEval import lineEval
import matplotlib.pyplot as plt


def driver():
    
    f = lambda x: math.exp(x)
    a = 0
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
        fex[j] = f(xeval[j]) 
      
    plt.plot(xeval,fex,'g',label='exact')
    plt.plot(xeval,yeval,'b',label='linear spline')
    plt.legend()
    plt.show()   

    err = abs(yeval-fex)
    plt.cla()
    plt.plot(xeval,err,'r',label='absolute error')
    plt.legend()
    plt.show()            
    
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    
    for jint in range(Nint):
        # '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        # '''let ind denote the indices in the intervals'''
        # '''let n denote the length of ind'''
        
        # '''temporarily store your info for creating a line in the interval of 
        #  interest'''
        a1 = xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        
        for kk in range(Neval):
           '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
           yeval[kk] = lineEval(xeval[kk],(a1,fa1),(b1,fb1))
           # this line modified
    return yeval
           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
