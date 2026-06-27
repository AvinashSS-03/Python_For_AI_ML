#Iterator: An iterator is an object that allows you to access elements of a collection one at a time using next().
# It is useful for memory-efficient processing, especially when working with large datasets, files, or streams of data.
'''
Advantages
 Memory efficient
 Good for large datasets
 Reads one element at a time
 Used internally by for loops and file handling
Disadvantages
 Cannot move backward
 Raises StopIteration when finished
 Cannot be reused after it is exhausted
 Slightly more complex than using a for loop
'''
a=[3,4,5,6,7]
c=iter(a)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

