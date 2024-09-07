import numpy as np
import matplotlib.pyplot as plt

d = np.array([10**i for i in range(-16,1,1)])
# values of delta
f = lambda x: np.cos(x+d) - np.cos(x)
# cos(x+d)-cos(d)
g = lambda x: -2*np.sin(x + d/2)*np.sin(d/2)
# manipulated cos(x+d)-cos(d)
#g = lambda x: abs(-2*np.sin(x + d/2)*np.sin(d/2) - np.cos(x+d) + np.cos(x))
# difference function
x1 = np.array([np.pi]*len(d))
x2 = np.array([10**6]*len(d))
# values of x to use

for xvals,title,marker,name in zip([x1,x2],["$x=\pi$","$x=10^6$"],['bo','go'],['1_Q5b','2_Q5b']):
    plt.semilogx(d,g(xvals)-f(xvals),marker,markersize=3)
    plt.ylabel('Difference')
    plt.xlabel('$\delta$',fontsize=15)
    plt.title(title)
    plt.savefig(name)
    plt.clf()

plt.semilogx(d,g(x1)-f(x1),'bo',markersize=3,label='$x=\pi$')
plt.semilogx(d,g(x2)-f(x2),'go',markersize=3,label='$x=10^6$')
plt.ylabel('Difference')
plt.xlabel('$\delta$',fontsize=15)
plt.legend()
plt.savefig('3_Q5b')