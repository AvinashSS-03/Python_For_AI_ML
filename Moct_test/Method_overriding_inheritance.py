#demonstrate method ovverriding using inheritance
from symtable import Class


class P:
    def vo(self):
        print("My vehicle is")
class c(P):

    def vo(self):
        super().vo()
        print("car")
class b(P):

    def vo(self):
        super().vo()
        print("Bike")
obj1=c()
obj1.vo()