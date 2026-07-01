#generator in Python is a special type of function that produces values one at a time instead of returning all values at once.
#It uses the yield keyword instead of return.

def y():
    yield 1
    yield 2
    yield 3
gen =y()
print(gen)  #This prints the Object space
print(next(gen))  # yield is used to return keyword instead of return
print(next(gen))
print(next(gen))

