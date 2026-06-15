lst=[1,2,3,4,5,6,7]
lst2=[2,3,7,5,8]
result=[]
for i in lst:
    if i in lst2:
        result.append(i)
print(result)