#with is used to close the file automaticlly we do not need to use close all time
'''
syntax:
 with open("Filename.Format","Mode") as variable
 variable.mode()
'''

with open("test.txt",'r') as e:
    print(e.read())
print(e.closed)


