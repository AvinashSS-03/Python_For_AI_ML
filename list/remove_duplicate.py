lst=[1,1,2,2,3,3,4,5,6,4,5,6]
result=[]

for i in lst:
    if i not in result:
        result.append(i)
print(result)