n=int(input())
count=0
v=n//2
for i in range(1,v+1):
    if n%i==0:
        count+=1

if count>1:
        print("this is not a prime number")
else:
        print("this is a prime number")