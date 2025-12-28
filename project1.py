'''PROJECT 1 — Student Management System (Python Only)

👉 Features:
Add student (name, age, marks)
Search student by name
Update marks
Delete student
Show all students
Save data into a file
Load data from file
'''
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    def disp(self):
        print(f"student name is {self.name} and age is {self.age} and marks is {self.marks}")
        
class Studentmanasyst:
    def __init__(self):
        self.students=[]

    def addstud(self,name,age,marks):
        self.students.append(Student(name,age,marks))
        print('Added successfully')
    
    def serstud(self,namee):
        for s in self.students:
            if s==namee:
                print(f"student name is {self.name} and age is {self.age} and marks is {self.marks}")
            else:
                print("Name is not found")
    
    def updstud(self,name,updmarks):
        for s in self.students:
            if s==name:
                self.marks=updmarks
    
    
