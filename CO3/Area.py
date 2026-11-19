from Graphics.RectFunctions import *
from Graphics.CirFunctions import *
from Graphics.DGraphics.SphereFunctions import *
from Graphics.DGraphics.CubiodFunctions import *

l=int(input("enter lenght:"))
b=int(input("enter breadth:"))
print("rectangle area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))

r=int(input("enter the radius of circle:"))
print("circle area=",CirArea(r))
print("circle Perimeter=",CirPerimeter(r))

r=int(input("enter radius of the sphere:"))
print("sphere area=",SpArea(r))
print("sphere volume=",SpPerimeter(r))

l=int(input("enter cube lenght"))
b=int(input("enter cube breadth"))
h=int(input("enter cube hieght"))
print("cubiod area=",CubArea(l,b,h))
print("cubiod Perimeter=",CubPerimeter(l,b,h))
