# Method Overriding
# If there are two methods with same name and same number of parameters but in different class
# And one method inherits from another method

class A:

    def show(self):
        print("executed show from class A")

class B(A):
    #pass #executed show from class A
    def show(self): # This show method overrides the show method inherited from class A
        print("executed show from class B")

b1= B()
print(b1.show())
        

