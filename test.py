class Student:
    marks = []
    def getData(self,rn,name,m1,m2,m3):
        Student.rn=rn
        Student.name=name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
    def displayData(self):
        print ('Access Number is: ',Student.rn)
        print ('Name is: ',Student.name)
        print ('Marks are: ',Student.marks)
        print ('Total marks are:',self.total())
        print ('average marks are:',self.average())
    def total(self):
        return (Student.marks[0] + Student.marks[1] + Student.marks[2])
    
    def average(self):
        return((Student.marks[0] + Student.marks[1] + Student.marks[2])/3)
a=  (input('Enter the access number: '))
name = input ('enter the name: ')
m1 = int(input ('enter the marks in first test:') )   
m2 = int(input ('enter the marks in second test:') )
m3 = int(input ('enter the marks in third test:') )

s1 = Student()
s1. getData(a,name,m1,m2,m3)
s1.displayData()