# Lab 12

import numpy as np

def eval_composite_trap(a,b,f,Npts):
# calcs composite trapezoid quadrature

    h = (b-a)/Npts
    quad = f(a)
    for ii in range(1,Npts-1):
        quad += 2.0*f(a+ii*h)
    quad += f(b)

    return 0.5*quad*h

def eval_composite_simpsons(a,b,f,Npts):
# calcs composite simpsons quadrature

    Xs = np.linspace(a,b,Npts+1)
    
    if Npts%2 == 1:
        print('error: Simpsons requires n is even')
        return 0
        
    h = (b-a)/Npts
    quad = f(a)
    for ii in range(1,Npts//2-1):
        quad += 2.0*f(a + 2*ii*h)
    for ii in range(Npts//2):
        quad += 4.0*f(a + (2*ii+1)*h)
    quad += f(b)

    return quad*h/3

f = lambda x: x**2
print(eval_composite_simpsons(0,1,f,40))
    