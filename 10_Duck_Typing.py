# If a bird walking like a duck, quaking like a duck and swimming like a duck, then it is duck.
# If any bird matching with behavouir of a duck is a duck

# Dynamic typing : type of a variable can be mentioned later

class Spyder: #This is an IDE for Python, IDE - integrated development environment

    def execute(self):
        print("Spyder Compiling")
        print("Spyder Running")

class Jupyter: # Choosing different IDE

    def execute(self):
        print("Jupyter Compiling")
        print("Jupyter Running")
   
class Laptop:

    def code(self,ide): #ide is needed to excute the code, Here ide can be of type int,str,float.(type is not fixed)
        ide.execute()
#ide type can be anything but method should contain execute, then it works.

ide= Jupyter()
#ide= Spyder()

s1= Laptop()
s1.code(ide)