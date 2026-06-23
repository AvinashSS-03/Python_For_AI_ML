#using constructor a small student apllication


class student:
    def __init__(self,name,id):
        self.student_name=name
        self.student_id=id
    def display(self):
        print("Student name: ",self.student_name)
        print("Student id: ",self.student_id)

name=input("Enter student name: ")
id=int(input("Enter student id: "))

ob=student(name,id)    #object created
ob.display()