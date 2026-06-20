a={"Lorry","Bus","Bike"}
b={"imax","inox","broadway","bike"}

#if you want to add elements in a list we can use add

a.add("Car")
print(a)

#to update we can use update update is used to add multpile elements
b.update("pvr","cinepople","car")
#this will updaate as char only

b.remove("imax") #used to remove elements
# print(b)

#discard used to remove an element no error if the element is not present
a.discard("avinash")
print(a)

#pop is used to remove any random element and return
b.pop()
#print(b)

#clear is used to remove all the elements in the tuple
b.clear()
print(b)
b.add("avinash")
#union is used to combine two sets
a.union(b)
print(a)
#intersection() is used to returrn common elements
a.intersection(b)
print("intersection: ",a)

#differenence:element in the fordst but not the seonccd
a.difference(b)
