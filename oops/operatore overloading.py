#in python we do not support method overloading instead we use operatore overloading
# *,**-*args,*kargs
#*args-used to store tuple values
#**kargs -used to store paired values dictionary

class ov:
    def load(self,*a):
        print(type(a))
    def arg(self,*args):
        print(type(args))
obj=ov()
obj.arg(1,2,3,4,5)
obj.load(2,3,4,5,6)

class test:
    def lo(self,**kwargs):
        print(kwargs)
ob=test()
ob.lo(a="avinash",b="Amuu",c="Anukul")