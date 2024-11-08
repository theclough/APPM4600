# HW 10
import numpy as np
import matplotlib.pyplot as plt

McL = lambda x: x - x**3/6 + x**5/120
# McLaurin series for sin(x)
Pa = lambda x: (30*x + x**3)/(30 + 6*x**2)
Pb = lambda x: 180*x/(180 + 30*x**2 - 31*x**4)
Pc = lambda x: (30*x + x**3)/(30 + x**2)
# Pade approxes from parts a,b,c
funcs = [McL, Pa, Pb, Pc]
labels = ['McLaurin', 'Pade, a', 'Pade, b', 'Pade, c']
# for plotting in loop
xVals = np.linspace(0,5,100)
# plt.plot(xVals,np.sin(xVals),'k-',label='sin(x)')
# for func,labal in zip(funcs,labels):
#     plt.plot(xVals,func(xVals),label=labal)
# plt.title('Function Values')
# plt.ylim([-3,10])
# plt.legend()
# plt.show()

xVals = np.append(np.linspace(0.0628,3.14,49),np.linspace(3.2028,5,50))
sinVals = np.sin(xVals)
relErrors = [np.abs(sinVals-func(xVals)) for func in funcs]
for error,labal in zip(relErrors,labels):
    plt.plot(xVals,error,label=labal)
plt.title('Absolute Error')
plt.ylim([-0.5,10])
plt.legend()
plt.show()