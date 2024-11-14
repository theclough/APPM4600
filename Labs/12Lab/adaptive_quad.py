# get lgwts routine and numpy
from gauss_legendre import *

# adaptive quad subroutines
# the following three can be passed
# as the method parameter to the main adaptive_quad() function

def eval_composite_trap(Npts,a,b,f):
  # put code from prelab with same returns as gauss_quad
  # you can return None for the weights

    Xs = np.linspace(a,b,Npts+1)
    h = (b-a)/Npts
    quad = f(a)
    for ii in range(1,Npts-1):
        quad += 2.0*f(a+ii*h)
    quad += f(b)

    return 0.5*quad*h,Xs,None

def eval_composite_simpsons(Npts,a,b,f):
  # put code from prelab with same returns as gauss_quad
  # you can return None for the weights

    Xs = np.linspace(a,b,Npts+1)

    # if Npts%2 == 1:
    #     print('error: Simpsons requires n is even')
    #     return 0
        
    h = (b-a)/Npts
    quad = f(a)
    for ii in range(1,Npts//2-1):
        quad += 2.0*f(a + 2*ii*h)
    for ii in range(Npts//2):
        quad += 4.0*f(a + (2*ii+1)*h)
    quad += f(b)

    return quad*h/3,Xs,None


def eval_gauss_quad(M,a,b,f):
  """
  Non-adaptive numerical integrator for \int_a^b f(x)w(x)dx
  Input:
    M - number of quadrature nodes
    a,b - interval [a,b]
    f - function to integrate
  
  Output:
    I_hat - approx integral
    x - quadrature nodes
    w - quadrature weights

  Currently uses Gauss-Legendre rule
  """
  x,w = lgwt(M,a,b)
  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def adaptive_quad(a,b,f,tol,M,method):
  """
  Adaptive numerical integrator for \int_a^b f(x)dx
  
  Input:
  a,b - interval [a,b]
  f - function to integrate
  tol - absolute accuracy goal
  M - number of quadrature nodes per bisected interval
  method - function handle for integrating on subinterval
         - eg) eval_gauss_quad, eval_composite_simpsons etc.
  
  Output: I - the approximate integral
          X - final adapted grid nodes
          nsplit - number of interval splits
  """
  # 1/2^50 ~ 1e-15
  maxit = 50
  left_p = np.zeros((maxit,))
  right_p = np.zeros((maxit,))
  s = np.zeros((maxit,1))
  left_p[0] = a; right_p[0] = b;
  # initial approx and grid
  s[0],x,_ = method(M,a,b,f);
  # save grid
  X = []
  X.append(x)
  j = 1;
  I = 0;
  nsplit = 1;
  while j < maxit:
    # get midpoint to split interval into left and right
    c = 0.5*(left_p[j-1]+right_p[j-1]);
    # compute integral on left and right spilt intervals
    s1,x,_ = method(M,left_p[j-1],c,f); X.append(x)
    s2,x,_ = method(M,c,right_p[j-1],f); X.append(x)
    if np.max(np.abs(s1+s2-s[j-1])) > tol:
      left_p[j] = left_p[j-1]
      right_p[j] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j] = s1
      left_p[j-1] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j-1] = s2
      j = j+1
      nsplit = nsplit+1
    else:
      I = I+s1+s2
      j = j-1
      if j == 0:
        j = maxit
  return I,np.unique(X),nsplit

