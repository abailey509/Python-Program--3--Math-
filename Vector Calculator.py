# Written By: Andrew Bailey
# CS 246

import math

class Vector:
    def __init__ (self, i = 0, j = 0, k = 0):
        self.i = i
        self.j = j
        self.k = k

    def __str__ (self):
        return ("%d %d %d"%(self.i, self.j, self.k))

    def __repr__(self):
        return ("%d %d %d"%(self.i, self.j, self.k))

    def __add__(self, v):
        return Vector(self.i + v.i, self.j + v.j, self.k + v.k)
   
    def __sub__ (self, v):
        return Vector(self.i - v.i, self.j - v.j, self.k - v.k)

    def Cross(self, v):
        rI = self.j * v.k - self.k * v.j
        rJ = self.k * v.i - self.i * v.k
        rK = self.i * v.j - self.j * v.i
        return Vector(rI, rJ, rK)
    def Mag(self):
        return math.sqrt(self.i**2 + self.j**2 + self.k**2)


x1 = int(input("Enter X coordinate for Vector 1: "))
y1 = int(input("Enter Y coordinate for Vector 1: "))
z1 = int(input("Enter Z coordinate for Vector 1: "))

x2 = int(input("Enter X coordinate for Vector 2: "))
y2 = int(input("Enter Y coordinate for Vector 2: "))
z2 = int(input("Enter Z coordinate for Vector 2: "))


v1 = Vector(x1, y1, z1)
v2 = Vector(x2, y2, z2)

def Add(v1, v2):
    return(v1 + v2, )
            
def Sub(v1, v2):
    return(v1 - v2, )
            
def Cross(v1, v2):
    return(v1.Cross(v2), )

def Mag(v1, v2):
    return(v1.Mag(), v2.Mag())

def Default():
    print("Incorrect Selection")
            

dict = {
    1 : Add(v1, v2),
    2 : Sub(v1, v2),
    3 : Cross(v1, v2),
    4 : Mag(v1, v2),
}


again = "y" 

while again == "y":

    print ("Press corresponding number to select an operation: \n1. Vector Addition \n2. Vector Subtraction \n3. Cross Product")
    print ("4. Vector Magnitudes")

    selection = int(input("Enter Selection: "))
    
    print(dict[selection][0])

    if selection == 4:
        print(dict[selection][1])

    again = input("Would you like to preform another operation? (y/n): ")

    if again == "n": 

        again = 0
        
