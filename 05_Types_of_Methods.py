# Types of Methods
# 1. Instance Methods 2.Class Methods 3.Static 
# 1. Instance Methods ------> i) Accessor Method ii) Mutator Method
# Accessor Method is used to fetch the values
# Mutator Method is used to modify the 

# 'self' is used when working with Instance variable
# 'cls' is used when working with Class variable

# Method that has nothing to do with the instance variable and class variable, then
# Static Method is used
# This is used to perform operations of other class objects. Ex: find the factorial of a number

class Students:
    school = 'Telugu Badi' #Class variable

    def __init__(self,m1,m2,m3): #METHOD
        self.m1=m1 #Instance variable are used for Instance methods
        self.m2=m2 #Instance variable
        self.m3=m3

    def avg(self): #METHOD, avg method is called Instance method because it works with object
        return (self.m1+self.m2+self.m3)/3
    
    #Accessor method, ex: To fetch the value of m1
    def get_m1(self): # Acessor METHOD # Getter
        return self.m1
    
    def set_m2 (self, value): # Mutator Method, # Setter
        self.m2 = value

    @classmethod #Decorator for class method
    def get_school_name (cls): # Class method, working with class variables
        return cls.school
    
    @staticmethod  #Decorator for static method
    def info():#Static method # No self and No cls #Nothing todo with Instance and class Variable
        print("This is from Static Method")

#Object
s1=Students(89,99,90) #passing a value

print(s1.avg())
print(s1.get_m1())
s1.set_m2(1000) # m2 value is set to 1000
print(s1.m2)
print(s1.avg()) # print average after m2 is set as 


print(Students.get_school_name()) # prints output of class method

Students.info() # prints output of static method
