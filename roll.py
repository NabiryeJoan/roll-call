# class Student:
#     def __init__(self,name):
#         self.name = name 
#         self.marks = []
        
#     def enterMarks(self):
#         for i in range(3):
#             m=int(input('enter the marks of %s in %d subject: '%(self.name,1+1)))
#             self.marks.append(m)
#     def display(self):
#         print(self.name, 'got', self.marks)
# name = input('enter the name of sudent:')
# s1=Student(name)

# s1.entermarks()
# s1.display()
class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
        
    def entermarks(self):
        for i in range(3):
            m = int(input('Enter marks of %s in %d of the subject: '%(self.name,1+1)))
            self.marks.append(m)
            
    def display(self):
        print(self.name, 'got', self.marks)

name = input("Enter the name of student:")
s1=Student(name)
s1.entermarks()
s1.display()
# s2=Student(name)
# s2.entermarks()
# s2.display()
