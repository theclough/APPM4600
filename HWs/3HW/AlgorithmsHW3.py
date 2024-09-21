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

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    results = [-1]
    count = 0
    while (count <Nmax):
        count = count +1 
        try:
            x1 = f(x0)
            results += [x1]
            if (abs(x1-x0) <tol):
                xstar = x1
                ier = 0
                return [xstar,ier,results[1::]]
            x0 = x1
        except:
            print('error: ',x0)
            break
    xstar = x1
    ier = 1
    return [xstar, ier, results[1::]]

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def compute_order(pStar,pVec,opt):
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
    coeffs = np.polyfit(np.log(diff2).flatten(),np.log(diff1).flatten(),1)
    # finds coeffs for log(p_{n+1}-p) = a*log(p_n-p) + log(l)
    # i.e.                  y         = c1*x          +  c2

    print('-----------------------')
    print(opt)
    print('log(|p_{n+1}-p|) = log(l) + a*log(p_n-p)')
    print('from ^ the order of the equation is: ')
    print('lambda = ', str(np.exp(coeffs[1])))
    print('alpha = ', str(coeffs[0]))
    # print results

    return [coeffs, diff1, diff2]