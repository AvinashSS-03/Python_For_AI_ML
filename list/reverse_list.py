lst=[1,2,3,4,5,6,7,8,9]
n=len(lst)
result=[]
for i in range(n-1,-1,-1):
    result.append(lst[i])
print(result)