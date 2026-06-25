#Method overriding is when a child class provides its own implementation of a method that already exists in the parent class, using the same method name and the same parameters.

class over:
    def ride(self):
        print("Welcome")
class o(over):
    def ride(self):
        # super().ride()
        print("to python")
obj=o()
obj.ride()
# if we want to inhert parent class methods we can use super keyword