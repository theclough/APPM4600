import numpy as np
import matplotlib.pyplot as plt

d = np.array([10**i for i in range(-16,1,1)])
# values of delta
f = lambda x: -2*np.sin(x + d/2)*np.sin(d/2)
# manipulated cos(x+d)-cos(d)
g = lambda x: f(x) - np.cos(x+d) + np.cos(x)
# difference function
a = lambda x: np.cos(x+d) - np.cos(x)
x1 = np.array([np.pi]*len(d))
x2 = np.array([10**6]*len(d))
# values of x to use

plt.semilogx(d,f(x2),'ro')
plt.savefig("testpng")

#-----

plt.figure()
plt.semilogx(d,f(x1)-a(x1),'go')
plt.xlabel("$\delta$", fontsize=15)
plt.ylabel("Difference", fontsize=10)
plt.title("$x=\pi$")
plt.savefig('1c_5b.png')
plt.clf()

plt.figure()
plt.semilogx(d,f(x1)-a(x1),'go')
plt.xlabel("$\delta$", fontsize=15)
plt.ylabel("Difference", fontsize=10)
plt.title("$x=\pi$")
plt.savefig('1c_5b.png')
plt.clf()

plt.figure()
plt.semilogx(d,g(x2),'bo')
plt.xlabel("$\delta$", fontsize=15)
plt.ylabel("Difference", fontsize=10)
plt.title("$x=10^6$")
plt.savefig('2_5b.png')