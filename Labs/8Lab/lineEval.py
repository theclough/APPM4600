# Pre-Lab for Lab 8
# algorithm that returns value of secant line from (x1,y1),(x2,y2)
# at a given point a

def lineEval(a,p1,p2):
# Inputs:
#     -a: point along line
#     -p1: (x1,y1)
#     -p2: (x2,y2) not = (x1,y1)
# Output:
#     -f(a): secant line evaluated at a
    
    x1,y1 = p1; x2,y2 = p2
    m = (y2-y1)/(x2-x1)

    return m*(a-x1)+y1

def test():
# tests lineEval()

    p1 = (0,0); p2 = (2,2);
    print(lineEval(1,p1,p2),' : should be 1')

    p1 = (0,0); p2 = (2,4);
    print(lineEval(1,p1,p2),' : should be 2')