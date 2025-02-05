class MyClass:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()
        

    def printString(self):
        print(self.str.upper())

stringinputoutput = MyClass()
stringinputoutput.getString()
stringinputoutput.printString()


##############################################################

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

shape = Shape()
print(f"Area of shape: {shape.area()}") 

square = Square(12)
print(f"Area of square: {square.area()}")  

##############################################################




class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width
    

rect = Rectangle(5,20)

print(f"Area of rectangle: {rect.area()}")  



##############################################################


import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f'X:{self.x} Y:{self.y}')


    def move(self, dx, dy):
        self.x += dx
        self.y += dy


    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

point1 = Point(3, 4)
point1.show() 

point2 = Point(6, 8)
point2.show() 

distance = point1.dist(point2)
print(f"Distance: {distance}")  

point1.move(2, 3)
point1.show()

distance = point1.dist(point2)
print(f"Distance: {distance}")  

##############################################################



class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit: {amount}. Balance: {self.balance}")
        else:
            print("Deposit amount must be positive")


    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal of {amount:2f} exceeds available balance. Current balance: {self.balance:.2f}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive.")

myaccount = Account("Sofiya", 100)

myaccount.deposit(50)  
myaccount.deposit(25)  

myaccount.withdraw(30)  
myaccount.withdraw(200)  
myaccount.withdraw(15)  


##############################################################




