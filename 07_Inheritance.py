# Inheritance
# Example: Parents house is childrens house, children inherit from parent
# All OOP have inheritance
# Inheritance : using features of existing class

# Single level inheritance
# Lets say A, B, C are different classes
# In single level B inherits all features from A 
# class(A)------>class(B)

# Multi level inheritance
# C inherits all features from B. here B has already inherited features from A.
# So C will all features that are in A and 
# class(A)------>class(B(A))[contains features inherited from A]------->class(C(B))[contains features inherited from B and A]

# Multiple Inheritance
# A has some features and B has some other features. C inherits all features
# Class(A)---No inheritance-->Class(B)------->Class C (A,B) [Contains all features from B and A]


class A: # Parent class or Super Class # Super class cannot access features of sub class
    def features1(self):
        print("Features 1 woking")

    def features2(self):
        print("Features 2 woking")

class B(A): # inheriting features from Class A #B is child Class or Sub class
    def features3(self):
        print("Features 3 woking")

    def features4(self):
        print("Features 4 woking")

class C: #No inheritance
    def features5(self):
        print("Features 5 woking")

    def features6(self):
        print("Features 6 woking")

class D(B,C): # inheriting features from Class A,B,C
    def features7(self):
        print("Features 7 woking")
        
a1=A() #constructor of object
b1=B()
c1=C()
d1=D()

#d1. shows all features 1 to 7 , as it is inherited all features from A,B,C

 