import time as t
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import matplotlib.pyplot as plt

def driver():

    Exercises1()
    
    return

def Exercises1():

    times = {'LU': {'construct': np.zeros(6), 'solve': np.zeros(6)}, 'Solver': np.zeros(6)}
    ct = 0
    
    for N in [100,500,1000,2000,4000,5000]:
        # set up system 
        b = np.random.rand(N,1)
        A = np.random.rand(N,N)
        
        # compute LU
        t0 = t.time()
        P,L,U = scila.lu(A)
        tf = t.time()
        times['LU']['construct'][ct] = tf-t0

        # solve with LU (time)
        t0 = t.time()
        y = scila.solve(L,P@b)
        x = scila.solve(U,y)
        tf = t.time()
        times['LU']['solve'][ct] = tf-t0

        # solve with .sove (time)
        t0 = t.time()
        x = scila.solve(A,b)
        tf = t.time()
        times['Solver'][ct] = tf-t0

        # add to times dict
        ct += 1

    totals = times['LU']['construct'] + times['LU']['solve']
    plt.plot(range(6),times['Solver'],'bo',label='solver')
    plt.plot(range(6),totals,'ko',label='lu-total')
    plt.plot(range(6),times['LU']['solve'],'ro',label='lu-solve')
    plt.plot(range(6),times['LU']['construct'],'go',label='lu-construct')
    plt.legend()
    plt.xticks([])
    plt.xlabel('N = size of system')
    plt.ylabel('time (s)')
    plt.show()

driver()