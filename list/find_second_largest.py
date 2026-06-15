lst=[1,2,3,4,5,6,7,8]
n=len(lst)
lar=lst[0]
second=lst[0]
for i in range(0,n):
      if lst[i]>lar:
          second=lar
          lar=lst[i]
      elif lst[i]>second and lst[i]!=lar:
          second=lst[i]
print(lar)
print(second)
