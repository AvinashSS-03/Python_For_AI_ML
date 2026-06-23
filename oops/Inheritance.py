#Inheritance --> Inherit properties from one class to another class
'''
Types of Inheritance:
             -->Single
             -->multiple
             -->multilevel
             -->Hiearchial
             -->hybrid
'''


#Single Inheritance
'''
        Parent class
           |
           |
        Child class
'''
def single():
    class single_inheritance:
        def __init__(self):
            n=input("Father's Name: ")
            v=input("Mother's Name: ")
            self.n=n
            self.v=v
    class student1(single_inheritance):
        def display(self,student_name):
            print("Student Name: ",student_name)
            print("Father's Name: ",self.n)
            print("Mother's Name: ",self.v)
    obj=student1()
    obj.display("Bhuvana")
single()

'''
Multilevel inheritance:
              Grand parent
                   |
                   |
                Parent
                   |
                   |
                Child
                
'''
def multilevel():
    class grandparent:
         def __init__(self):
             n=input("Enter GrandFather Name: ")
             v=input("Enter Grandmother Name: ")
             self.Grandfather=n
             self.Grandmother=v
    class parent(grandparent):
         def __init__(self):
             super().__init__()
             n=input("Enter Father's Name: ")
             v=input("Enter Mother's Name: ")
             self.father=n
             self.mother=v


    class child(parent):
        def display(self,name):
            print("Student name: ",name)
            print("Father's Name: ",self.father)
            print("Mother's Name: ",self.mother)
            print("GrandFather's Name: ",self.Grandfather)
            print("GrandMother's Name: ",self.Grandmother)

    obj=child()
    obj.display("Bhuvana")
#multilevel()

