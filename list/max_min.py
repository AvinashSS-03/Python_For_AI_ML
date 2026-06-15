lst=[33,2,3,4,5,6,-1,7,8,9,10]
n=len(lst)
max=lst[0]
min=lst[0]
for i in range(0,n):
    if lst[i]>max:
        max=lst[i]
    elif lst[i]<min:
        min=lst[i]

print(max)
print(min)