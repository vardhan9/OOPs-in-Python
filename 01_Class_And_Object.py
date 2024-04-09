#Class contains attributes(variables) and behaviour(methods)
class Computer: 
    def configure(self): #def is to define method
        print("Thinkpad, Razeon, 32Gb RAM")

# creating com1 object
com1 = Computer() #OBJECT
#In JAVA this is called constructor

Computer.configure(com1) # Calling METHOD, Class.Method(object)
#To use method, need to use Class name
# Calling configure and pass com1 as 
# Prints Thinkpad, Razeon, 32Gb 

com1.configure() # using Object itself calling method, This takes object as parameter
#This type is most oftenly used

print(type(com1))
# Prints <class '__main__.Computer'> means com1 belongs to computer class

a="7"
b= 7
print(type(a),type(b))
# prints <class 'str'> <class 'int'>, str and int are inbuilt classes