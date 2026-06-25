# a="number" #-->This raises a TypeError
  #instead of string if you give anything then that raises value error
try:
    a = int(input("Enter  a numer"))
    a/5
    #a/0 -->this return It is not divisble
except ValueError:
    print("enter a integer")
except:
    print("It is not divisible")
finally:
    print("Operation completed")