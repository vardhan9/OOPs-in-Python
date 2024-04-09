# In OOPS, there are two different variables
# 1.Instance variable 2.Class(static) variable
# Instance variable : As object changes these values also changes. ex: Car and human are different objects
# If a value of one object is changed, it will not affect other objects
# If you define variable inside __init__, it is a instance 

# 2. Class Variable: defined outside __init__ and inside the 
# This is will same for all objects in the class. ex: car has four wheels

# namespace is an area where you create and store object/variable
# Class namespace
# Object/Instance namespace

class car:
    wheels = 4 # Class variable, shared between all objects
    def __init__(self):
        self.mileage= 20 #instance variable
        self.brand="mahindra" #instance variable

c1=car()

print(c1.mileage,c1.brand,car.wheels)

c2=car()
c2.mileage=18
c2.brand="tata"
car.wheels=5
print(c2.mileage,c2.brand,car.wheels)
      