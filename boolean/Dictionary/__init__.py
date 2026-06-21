# A dictionary is a Advanced data type in python which is
#mutable
#unorder
#indexing
#dictionary syntax {}
dit={"key":"value"}
print(dit)
print(type(dit))

d={"roll no:1":"kumar","roll no 2:":"Yadav","roll no 3":"Sharma"}
#print keys   dictinoary
for i in d:
    print(i)
#to print values
for x in d.values():
    print(x)
#to check both the values use .item()
for o in d.items():
    print(o)

#Update a Value in dictinoary
d["roll no:1"]="Avinash"
print(d)

