a=4
for i in range (1,a+1):
    for j in range(1,i+1):
        print("*" ,end=" ")
    print()

print("While loop")

def wloop():
    a=1
    while(a<=4):
        b=1
        while(b<=a):
            print("*",end=" ")
            b+=1
        print()
        a+=1
wloop()