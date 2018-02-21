import math

def solve(a,b,c):
    y = (b**2) - (4*a*c)
    square_root = math.sqrt(y)
    x1 = (-b + square_root)/(2*a)
    x2 = (-b - square_root)/(2*a)
    print(x1)
    print(x2)
    return

solve(1,2,8)