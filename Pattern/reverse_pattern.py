a=4
for i in range(a,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("while loop")


def wloop():
    a=4
    while(a>0):
        b=1
        while(b<=a):
            print("*",end=" ")
            b+=1
        print()
        a-=1
wloop()