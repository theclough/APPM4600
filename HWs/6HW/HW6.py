import math
import time
import numpy as np
import numpy.linalg as la
import biggestFall as steep
import Q1_1


def evalF(x0, opt):
# evaluates F from Q2
# opt = 1: Q1, 2, Q2
    
    if opt == 1:
        x,y = x0
        return np.array([[x**2+y**2-4],
                  [math.exp(x)+y-1]])
    else:
    # opt == 2
        x,y,z = x0
        return np.array([x + np.cos(x*y*z) - 1,
                  (1-x)**(1/4) + y + 0.05*z**2 - 0.15*z -1,
                  -x**2 - 0.1*y**2 + 0.01*y + z - 1])
    

def newtons(J,tol,x0,Nmax=100):
# implements newton's method
# returns [ier, xstar, count]

    n = len(x0)
    x1 = np.zeros(n)
    for ii in range(Nmax):
        J1 = [[J[ii,jj](x0[0],x0[1],x0[2]) for jj in range(n)] for ii in range(n)]
        J2 = la.inv(J1) @ evalF(x0,2)
        x1 = x0 - np.transpose(J2)
        for jj in range(n):
        # stopping conditon:
        #   relative errors of each term below tolerance
            if abs(x1[jj]-x0[jj]) < tol:
                quit = 1
            else:
                quit = 0
        if quit:
            return [0, x1, ii]
        x0 = x1

    return [1,x0,Nmax]

def quasiNewton(J,tol,x0,Nmax=100):

    return 0
                

def evalNormSqrd(x0,x1):
# calculates (x1 - x0)^2 in 2 norm

    sum = 0
    for ii in range(len(x0)):
        sum += (x1[ii] - x0[ii])**2

    return math.sqrt(sum)

def approxJacobian(J,F,x0,x1):
# calculates A = approx Jacobian
#  
#   = J(x0) + [F(x1)-F(x0)-J(x0)](x1-x0)'/||x1-x0||_2^2

    n = len(x0)
    result = np.zeros([n,n])
    for ii in range(n):
        return

def Q2():
# Question 2
#   3 Methods

    # 1) Newtons

    # define Jacobian
    dfdx1 = lambda x,y,z: 1 - y*z*np.sin(x*y*z)
    dfdx2 = lambda x,y,z: -x*z*np.sin(x*y*z)
    dfdx3 = lambda x,y,z: -x*y*np.sin(x*y*z)
    dgdx1 = lambda x,y,z: -0.25*(1-x)**(-0.25)
    dgdx2 = lambda x,y,z: 1
    dgdx3 = lambda x,y,z: 0.10*z - 15
    dhdx1 = lambda x,y,z: -2*x
    dhdx2 = lambda x,y,z: -0.2*y + 0.01
    dhdx3 = lambda x,y,z: 1
    J = np.array([[dfdx1, dfdx2, dfdx3],
                  [dgdx1, dgdx2, dgdx3],
                  [dhdx1, dhdx2, dhdx3]])

    x0 = np.array([0,0.1,1])
    tol = 10**(-6)
    t0 = time.time()
    [ier, xstar, count] = newtons(J,tol,x0)

    print('HW 6 - Q2')
    print('------------------------------------------------------------------')
    print('Part 1 : Newton Only')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('actual root was used: ', x0)
    print('the error message reads: ', ier)
    print('the approximate root is: ', xstar)
    print('the number of iterations was: ', count)
    print('F(xstar) = ', evalF(xstar,2))
    
    x0 = np.array([0.1,0.2,1.1])
    tol = 10**(-6)
    [ier, xstar, count] = newtons(J,tol,x0)
    
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('perturb each root by just 0.1')
    print('the initial guess was: ', x0)
    print('the error message reads: ', ier)
    print('the approximate root is: ', xstar)
    print('the number of iterations was: ', count)
    print('F(xstar) = ', evalF(xstar,2))
    
    # 2) Steepest Descent

    x0 = np.array([-2,2,2])
    t0 = time.time()
    for ii in range(50):
        [xstar, gval, ier, count] = steep.steepestDescent(x0,tol)
    tf = time.time()
    
    print('------------------------------------------------------------------')
    print('Part 2: Steepest Descent Only')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('the initial guess was: ', x0)
    print('the error message reads: ', ier)
    print('the approximate root is: ', xstar)
    print('the number of iterations was: ', count)
    print('g(xstar) = ', gval)
    print('it took an average of ', f'{(tf-t0)/50:.4g}', '(s) over 50 trials')

    # 3) Steepest Descent and then Newtons
    t0 = time.time()
    for ii in range(50):
        [xstar1, gval, ier1, count1] = steep.steepestDescent(x0,0.5*10**(-2))
        [ier, xstar, count] = newtons(J,tol,xstar1)
    tf = time.time()
    print('------------------------------------------------------------------')
    print('Part 3: Steppest Descent, then Newtons')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('the initial guess for Steepest Descent was: ', x0)
    print('the Steepest Descent error message read: ', ier1)
    print('the Stepest Descent iterations was: ', count1)
    print('the initial guess for Newton was: ', xstar1)
    print('the Newton error message read: ', ier)  
    print('the Newton iterations was: ', count)
    print('the approximate root is: ', xstar) 
    print('it took an average of ', f'{(tf-t0)/50:.4g}', '(s) over 50 trials (for the combined method)')

def Q1():
# Question 3

    Q1_1.driver()

    # define Jacobian inverse
    f1 = lambda x,y: (2*x-2*y*np.exp(x))**(-1)
    f2 = lambda x,y: -y/(x-y*np.exp(x))
    g1 = lambda x,y: -np.exp(x)/(2*x-2*y*np.exp(x))
    g2 = lambda x,y: x/(x-y*np.exp(x))
    Jinv = np.array([[f1,f2],[g1,g2]])

    # initial guesses & tolerance
    x0s = np.array([[1,1],[1,-1]])
    tol = 10**(-6)

    # Broydens method
    print('Quasi Newton 2 : Broydens Method')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    for x0,i in zip(x0s,['(i)','(ii)']): 
        ier = 1; xstar = x0; count = 100;
        A = np.array([[Jinv[ii,jj](x0[0],x0[1]) for jj in range(2)] for ii in range(2)])
        v = evalF(x0,1)
        s = -A @ v
        x1 = x0 + np.transpose(s)
        x1 = x1[0]
        for ii in range(2,100):
            w = v
            v = evalF(x1,1)
            y = v - w
            z = -A @ y
            p = -np.transpose(s) @ z
            u = np.transpose(s) @ A
            A = A + ((s + z) @ u)/p[0,0]
            s = -A @ v
            x1 = x1 + np.transpose(s)
            x1 = x1[0]
            if np.sqrt(s[0]**2 + s[1]**2) < tol:
                ier = 0; xstar = x1; count = ii;
                break

        fstar = evalF(xstar,1)
        print('ICs ',i,':')
        print('the initial guess was: ', x0)
        print('the error message read: ', ier)
        print('the number of iterations was: ', count)
        print('the approximate root was: ', xstar)
        print('F(xstar) = ', [fstar[0][0],fstar[1][0]])
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    fstar = evalF([0,0],1) 
    print('ICs (iii):')
    print('the initial guess was: ', [0,0])
    print('Broylens also fails because the Jacobian is singular')
    print('F(x0) = ', [fstar[0][0],fstar[1][0]])
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

Q1()