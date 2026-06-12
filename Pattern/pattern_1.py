a=4
for i in range(1,a+1):
    for j in range(1,a+1):
        print(i,end="")
    print()

print("while loop")

def wloop():
    a=1
    while(a<=4):
        b=1
        while(b<=4):
            print(a,end=" ")
            b+=1
        a+=1
        print()

wloop()