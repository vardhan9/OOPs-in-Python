#Operators : + - x /

# ex: 5+6 , here 5,6 are operands and + is operator
# In operator overloading, operator remains same but operands change

a=5
b=6
print(a+b)

#The following will be happening in background
print(int.__add__(a,b))#__add__() is builtin method(magic methods) in python, int is 

#-------------------------------------------------------------------------------------#
#operator overloading

class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    # operator overloading, because builtin method does not works in this case 
    #builtin can add int,float,str
    # operator overloading canbe done only with builtin operators , as __add__ in this example
    def __add__(self,other): 
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=self.m3+other.m3
        s3 = student(m1,m2,m3)
        return s3
    
    def __gt__(self,other): # __gt__ is greater than
        s1marks = self.m1 + self.m2 + self.m3
        s2marks = other.m1 + other.m2 + other.m3
        if s1marks > s2marks:
            return True
        else:
            return 
    
    def __str__(self): #overloading __str__
        return '{} {} {}'.format(self.m1,self.m2,self.m3)
        


s1=student(99,56,89)
s2=student(88,65,78)

s3 = s1+s2 #----> student.__add__(s1,s2), this happens in background
# gives TypeError: unsupported operand type(s) for +: 'student' and 'student' without operator overloading
print(s3.m1,s3.m2,s3.m3)


# comparing students on total marks achieved

if s1 > s2: # TypeError: '>' not supported between instances of 'student' and 'student', so operator overloading is needed
    print("s1 wins")
else: 
    print("s2 wins")


x=11
print(x) #Prints values of x, x.__str__() calls this way
print(s1) # Prints <__main__.student object at 0x000001FA7D0F74D0> address
# when ever object is called, its calls as 'str' in background



