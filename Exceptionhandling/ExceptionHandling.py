# a="number" #-->This raises a TypeError
  #instead of string if you give anything then that raises value error
try:
    num = int(input("Enter  a numer"))
    num/5
    #a/0 -->this return It is not divisble
except ValueError:
    print("enter a integer")
except:
    print("It is not divisible")
finally:
    print("Operation completed")