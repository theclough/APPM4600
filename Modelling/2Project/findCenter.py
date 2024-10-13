import math

def findCenter(Xs,Ys):
# finds center of circle defined by 3 *different* points
# Inputs:
#     -Xs : array of x values
#     -Ys : array of y values
# Outputs:
#     (xC,yC) : tuple of coords for center
    x0,x1,x2 = Xs
    y0,y1,y2 = Ys
    # get points

    x1 -= x0; x2 -= x0;
    y1 -= y0; y2 -= y0
    # subtract off (x0,y0)
    
    xC = 0.5*(y1*(x2**2+y2**2)-y2*(x1**2+y1**2))/(x1*y2-x2*y1)
    yC = 0.5*(x1*(x2**2+y2**2)-x2*(x1**2+y1**2))/(x2*y1-x1*y2)
    # use formula (derived by treating (x0,y0) = (0,0))

    return (xC-x0,yC-y0)
    # put solution back in original coordinate system
    

def test():
# test function on unit circle (center : (0,0))
    
    f = lambda y,x=1: math.cos(math.pi*x/y)
    g = lambda y,x=1: math.sin(math.pi*x/y)
    
    Xs = [f(7),f(9),f(2)]
    Ys = [g(7),g(9),g(2)]
    
    print(findCenter(Xs,Ys))

test()