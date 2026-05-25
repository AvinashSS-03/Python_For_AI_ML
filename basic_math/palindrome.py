a=int(input())
b=a
reverse=0
while a!=0:
    d=a%10
    reverse=(reverse*10)+d
    a//=10
print(reverse)
if reverse==b:
    print("It is a plaindrome")
else:
    print("It is not a plaindrome")