#This program is used to find the element present only in class A
class_a = {"avinash", "ram", "kumar"}
class_b = {"ram", "surya", "kumar"}

only_a=class_a.difference(class_b)
print(only_a)