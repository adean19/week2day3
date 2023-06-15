from math import pi as p

def sqft_house():
    length = input("What's the length?")
    width = input("What's the width?")
    squareft = length * width
    print (squareft)

def circle_circum():
    r = input("From the middle of the circle to any point on the boundary, please provide the radius.")
    C = 2*p*r