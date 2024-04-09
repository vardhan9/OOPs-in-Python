class Computer: #Class

    def __init__(self,cpu,ram): #(com1,cpu,ram) , com1 parameter will be passed to self
        # Special method __init__
        # call automatically without calling
        # For every object it will be called once
        self.cpu=cpu #Here self is the object
        self.ram=ram
        print("init intialized")

    def configure(self): #Method
        print("Configure is ", self.cpu, self.ram)

com1=Computer('Rayzen','32 GB') #Object is com1, Computer() is object creation
com1.configure() #Calling Method
 
com2= Computer('M1', '1TB')
com2.configure() #Calling Method