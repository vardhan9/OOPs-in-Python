# Constructor in Inheritance
# Method Resolution Order (MRO)

class A:

    def __init__(self):
        print('Call init in A')

    def feature1(self):
        print ("Feature 1 working")

    def feature2(self):
        print ("Feature 2 working")

class B:
    def feature3(self):
        print ("Feature 3 working")
    def feature4(self):
        print ("Feature 4 working")

a1=A()
a1 # Calls Class A

#-----------------------------------------------------------------------------------------#

class C:
    
    def __init__(self):
        print('Call init in C')

    def feature1(self):
        print ("Feature 1 working")

    def feature2(self):
        print ("Feature 2 working")

class D(C):

    def __init__(self): # if this __init__ is removed then it call __init__ in 
        super().__init__() # This calls __init__ of superclass, Class C in this case
        print('Call init in D')

    def feature3(self):
        print ("Feature 3 working")
    def feature4(self):
        print ("Feature 4 working")

c1=D()
c1 # Calls Class C because __init__ is present in the class C



#-----------------------------------------------------------------------------------------#
#Method of Resolution Order --> MRO
# Order goes from left to right

class x:

    def __init__(self):
        print ("call init in x")

    def feature7(self):
        print ("Feature 7 working")

class y:

    def __init__(self):
        print ("Call init in y")

    def feature8(self):
        print ("Feature 8 working")

class z(x,y): # x,y both are super classes # x will be called because of MRO, Order starts from right

    def __init__(self):
        super().__init__() # Super Method to call super class
        print ("Call init in z")
    def feature9(self):
        print ("Feature 9 working")

    def feature10(self): # calling method of  with super  super class 
        super().feature7()
        

z1=z()
z1
z1.feature10()