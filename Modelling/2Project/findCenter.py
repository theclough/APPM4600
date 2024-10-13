import math

def findCenter(Xs,Ys, tol):
# finds center of circle defined by 3 *different* points
# Inputs:
#     -Xs : array of x values
#     -Ys : array of y values
#     -tol : tolerance check for 0
# Outputs:
#     (xC,yC) : tuple of coords for center
    x0,x1,x2 = Xs
    y0,y1,y2 = Ys
    # get points

    x1 -= x0; x2 -= x0;
    y1 -= y0; y2 -= y0
    # subtract off (x0,y0)
    
    xC = 0.5*(y1*(x2**2+y2**2)-y2*(x1**2+y1**2))/(x1*y2-x2*y1) - x0
    yC = 0.5*(x1*(x2**2+y2**2)-x2*(x1**2+y1**2))/(x2*y1-x1*y2) - y0
    # use formula (derived by treating (x0,y0) = (0,0))
    # - (x0,y0) to shift back into original coordinate system

    if xC < tol:
        if yC < tol:
            xC,yC = (0,0)
        else:
            xC = 0
    if yC < tol:
        yC = 0
    # check if xC and/or yC below tolerance
        
    return (xC,yC)
    

def test():
# test function on unit circle (center : (0,0))
    
    f = lambda y,x=1: math.cos(math.pi*x/y)
    g = lambda y,x=1: math.sin(math.pi*x/y)
    
    Xs = [f(3,4),f(1),f(2,3)]
    Ys = [g(3,4),g(1),g(2,3)]
    tol = 10**(-10)
    
    print(findCenter(Xs,Ys,tol))

test()