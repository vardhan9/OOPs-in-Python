# Class inside a Class
# In some cases we needed class inside a class
# you can create object of inner class inside the outer class
# OR
# You can create object of inner class outside the outer class provided you use outer class name to call it


class students(): #Class 1
    def __init__(self,name,rollno,age):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.lap=self.laptop() # calling class 2 from here
        
    def student_info(self):
        print(self.name, self.rollno, self.age)
        self.lap.laptop_info() # laptop information

    class laptop: #Class 2 (inner class)
        def __init__(self):
            self.brand = 'Apple'
            self.cpu = 'M2'
            self.memory = '1TB'
        
        def laptop_info(self):
            print(self.brand,self.cpu,self.memory)


s1=students('king',1,20)
s1.student_info()# prints student info from class 1

students.laptop()#Prints laptop infor from class 2 (inner class)