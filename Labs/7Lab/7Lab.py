# Tyler Clough, Lab 7
import numpy as np
import numpy.linalg as la

def driver():

    Exercises()

def callInterpol(n):
# n > 1

    interpol = np.zeros(n)
    h = 2/(n-1)
    for ii in range(n):
        interpol[ii] = -1 + (ii-1)*h

    return interpol
    

def determine_coeffs(p, interpol, n):
# finds coeffs, a1,...,an for n degree interpolation
#   -degree must be > 0
# with interpolation points [interpol]

    A = np.zeros([1,n+1,1,n+1])
    A[:,0] = 1
    for i in range(1,n+1):
        b[ii-1] = p(interpol[ii-1])
        for j in range(1,n+1):
            A[i][j] = (interpol[i])**j


    return A @ b

def Exercises():

#   3.1

    f = lambda x: 1/(1+100*x**2)
    interval = np.linspace(-1,1,1000)
    interpol = callInterpol(2)
    coeffs = determine_coeffs(f,interpol,2)
    coeffs

driver()