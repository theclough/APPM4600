import numpy as np
import matplotlib.pyplot as plt

d = np.array([10**i for i in range(-16,1,1)])
# values of delta
f = lambda x: abs(-2*np.sin(x + d/2)*np.sin(d/2))
# manipulated cos(x+d)-cos(d)
g = lambda x: abs(-2*np.sin(x + d/2)*np.sin(d/2) - np.cos(x+d) + np.cos(x))
# difference function
a = lambda x: abs(np.cos(x+d) - np.cos(x))
x1 = np.array([np.pi]*len(d))
x2 = np.array([10**6]*len(d))
# values of x to use

name = 1
for plot,ylabel in zip([a,f,g],["$\cos(x+\delta)-\cos(x)$","$-2\sin(x+\delta/2)\sin(\delta/2)$","Difference"]):
    for xvals,title in zip([x1,x2],["$x=\pi$","$x=10^6$"]):
        plt.loglog(d,plot(xvals),'go')
        plt.xlabel("$\delta$", fontsize=15)
        plt.ylabel(ylabel, fontsize=10)
        plt.title(title)
        plt.show()
        plt.clf()