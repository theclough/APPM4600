import numpy as np
import matplotlib.pyplot as plt

d = np.array([10**i for i in range(-16,1,1)])
# values of delta
f = lambda x: np.cos(x+d) - np.cos(x)
# cos(x+d)-cos(d)
g = lambda x: -2*np.sin(x + d/2)*np.sin(d/2)
# manipulated cos(x+d)-cos(d)
x1 = np.array([np.pi]*len(d))
x2 = np.array([10**6]*len(d))
# values of x to use

# (b)
for xvals,title,marker,name in zip([x1,x2],["$x=\pi$","$x=10^6$"],['bo','go'],['1_Q5b','2_Q5b']):
    plt.semilogx(d,g(xvals)-f(xvals),marker,markersize=3)
    plt.ylabel('Difference')
    plt.xlabel('$\delta$',fontsize=15)
    plt.title(title)
    plt.savefig(name)
    plt.clf()
# plots differences for x1 and x2 on different plots

# (c)
t = lambda x: -(np.sin(x) + d**2/2)
# upper bound derived from Taylor Series
for xvals,title,marker,name in zip([x1,x2],["$x=\pi$","$x=10^6$"],['bo','go'],['3_Q5b','4_Q5b']):
    plt.semilogx(d,t(xvals)-g(xvals),marker,markersize=3)
    plt.ylabel('Difference')
    plt.xlabel('$\delta$',fontsize=15)
    plt.title(title)
    plt.savefig(name)
    plt.clf()
# same as before but with expression from Taylor Series