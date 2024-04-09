# Method Overloading : class having two different methods with same name but different parameter
# But in Python we cannot create two methods with same name

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    #def sum(self.,a,b,c) this does not work if onöy two or one arguments are given. 
    def sum(self, a=None,b=None,c=None): # Method overloading , to work with two or one arguments
        s=0

        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!= None and b!=None:
            s=a+b
        else:
            s=a
        return s

s1=student(11,12)
print(s1.sum(1,2))