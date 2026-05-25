#important notes in python
""" casting:
           when numbers are assigned as string to the variable the outplut will be in string only
           ex:a=10
              b=20
              c=a+b
              output=1020 """
a="10"
b="20"
c=a+b
print(c)

""" if you want to change the string to int just add int before string int("string")"""
""" Automation and sheduling:
         python can automatically do the tast thart is called as auomation ex"sending an email,scraping webs,filling forms
         *Running a task at specific time is called scheduling """
"""
Variable scope:
            Local 
            Enclosing 
            Global
            built in
            """
"""
operators in python:
         ** -->multiply thae values like a=10 b=3 a**b means 10*10*10
         // -->when dividing the numbers will be in whole 
         and
         or 
         not 
"""
"""
comments in python:
         #-->single line comment
       """ """   --> Multi  line comments
"""
"""
Input handling
     a=input("Enter a number: )
     so basically input get the values as a string
"""
"""
Sys argv 
   this is used to store input values while running the program 
   used for automation
   instead of manual typing we use this sys.argv 
   this should be runned in terminal with some order
   python filename.py input
   sys.argv[0]	file name
   sys.argv[1]	first argument
   sys.argv[2]	second argument
"""
import sys

f = int(sys.argv[1])
e = int(sys.argv[2])

print(f+e)

"""So this can be used for automation like python filename datasset.csv if we give it will automatically take all the inputs from csv file"""

"""
String:
  single and double colon are considered as string no char is here like java
  Built-in-functions:
   .lower()
   .upeer()
   .capitalize()
   .To get first two digit[:2]
   .to get last tewo digit[-2:]
   .title() make capitle of first character in a word
   .replace(old,new)
   .split()
   .strip() -->remove spaces
   .find() -->used to find th positions of the words
   .alnum -->check alphanumeric
   
   """