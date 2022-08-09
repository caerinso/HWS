import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y 

class Rectangle(Point) :

    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    
    def get_area(self):
        a=self.p2.x-self.p1.x
        a=abs(a) 
        b=self.p2.y-self.p1.y
        b=abs(b) 
        return a*b

    def get_perimeter(self):
        a=self.p2.x-self.p1.x 
        a=abs(a)
        b=self.p2.y-self.p1.y
        b=abs(b)
        
        return 2*a+2*b

    def is_square(self):
        a=self.p2.x-self.p1.x 
        a=abs(a)
        b=self.p2.y-self.p1.y
        b=abs(b)
        return a==b

p1=Point(1,3)
p2=Point(3,1)
r1=Rectangle(p1,p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p1=Point(3,7)
p2=Point(6,4)
r1=Rectangle(p1,p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

