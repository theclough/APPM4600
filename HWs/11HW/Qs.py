# HW11, formatting for Q1 answers

from HW11 import *

def driver(opt):
    
    if opt == 1:
        a = -5; b = 5
        f = lambda s: 1./(1+s**2)   
        nPts = 2236
        exact = 2*math.atan(5)
        compT = eval_composite_trap(a,b,f,nPts)
        compTError = abs(exact - compT)
        spicyQ = spicy.quad(f,a,b,epsabs=0.0001)[0]
        printlines()
        print()
        print()
        print('Composite Trapezoid')
        printlines()
        print('exact integral value = 2*arctan(5) = ',exact)
        print('# of points in interval: ',nPts)
        print('approximate interval from Composite Trap: ',compT, '             ( absolute error = ', compTError,')')
        print('approximate interval from scipy quad() function: ',spicyQ)
        printlines()
        nPts = 114
        compT = eval_composite_simpsons(a,b,f,nPts)
        compTError = abs(exact - compT)
        print('Composite Simpsons')
        printlines()
        print('exact integral value = 2*arctan(5) = ',exact)
        print('# of points in interval: ',nPts)
        print('approximate interval from Composite Simpsons: ',compT, '          ( absolute error = ', compTError,')')
        print('approximate interval from scipy quad() function: ',spicyQ)
        print()
        print()
        printlines()

    if opt == 2:
        a = 10**(-10); b = 1
        f = lambda t: t*math.cos(1./t)   
        nPts = 6
        exact = 0.0181176 # approximate
        compT = eval_composite_simpsons(a,b,f,nPts)
        compTError = abs(exact - compT)
        print('--------------------------------------------------------------------------------------------')
        print()
        print()
        a = '                     '
        print(a+'Question 2')
        print('                    ------------------------------------------------------')
        print(a+'exact integral value ~ ',exact)
        print(a+'approximate interval from Composite Trap: ',f'{compT:.7f}')
        print(a+'absolute error = ', f'{compTError:.7f}')
        print()
        print()
        print('--------------------------------------------------------------------------------------------')
        
driver(2)