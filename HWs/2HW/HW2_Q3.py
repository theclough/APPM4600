import math

tol = 10**(-16)
x = 9.999999995000000*10**(-10)
y = 0
for ii in range(150):
    y += x**ii/math.factorial(ii)

print(y-1)