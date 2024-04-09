#Constructor and Self, Comparing Objects
# Every time you create an object, it is allocated in new space
# Size of an object depends on the no of variables and size of each variable
# Constructor allocates the memory
#compare : who is calling and whom to compare
class Comparison:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

person1 = Comparison("king",32)
person2= Comparison("queen",31)

print(person1.name,person1.age)
print(person2.name,person2.age)

if person1.compare(person2): #compare is not inbuilt function
    print("same age")
else:
    print("different age")


