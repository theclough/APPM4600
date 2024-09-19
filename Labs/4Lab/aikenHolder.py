import numpy as np

def aikenHolder(f,x0,tol,Nmax):
# test to see if can even
# get aiken to work
    fixedP = 1.3652300134140976
    [xstar,ier,results] = fixedpt(f,x0,tol,Nmax)
    pHat = results[2] - (results[0] - results[2])**2/(results[1] - 2*results[0] + results[2])
    pVec = [pHat]
    for ii in range(3,len(results[3:])):
        pHat += [results[ii+2] - (results[ii] - results[ii+2])**2/(results[ii+1] - 2*results[ii] + results[ii+2])]
    
    return [pVec[-1],ier,pVec]