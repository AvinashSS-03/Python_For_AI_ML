#file handling is used to handle the data in the file
#Mode - read(w),write(w),append(a),extension(x)

'''
Syntax:
    variable=open("filename.format,"Mode")
    variable.mode()
'''
from traceback import print_tb

v=open("test.txt",'r')
print(v.read())
v.close()
#this is used to read the contents in the list

o=open("test.txt",'w')
print(o.write("Welcome to python"))
o.close()#this will return the number of characters written in test file ,in this 17 characters were added
 #if the file is already created it deletes and overwite the content

 #append is used to add the content in the last of the text file
a=open("test.txt",'a')
a.write("version-3.5.2")
a.close()
#extensions -->used to create file
d=open("test1.txt",'x')
d.write("extension concept")
d.close()
#create a csv file

r=open("test2.csv",'x')
r.write("Extension concpet creating csv file")
r.close()

print(a.mode)
print(a.name)
print(a.closed)