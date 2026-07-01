#List comprehension is a short and Pythonic way to create a list from an iterable (like a list, range, or string).

nums=[i for i in range(1,6)]
print("List comprehension",nums)
# normal loop
n=[]
for i in range(1,6):
    n.append(i)

print("normal loop method", n)