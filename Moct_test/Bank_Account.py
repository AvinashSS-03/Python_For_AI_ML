class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #now this is a Private Variable
    def deposit(self,depo):
        self.__balance+=depo
        print("Deposit successfull")
    def withdraw(self,withd):
        self.__balance-=withd
        print("Withdraw Succesfull")
    def show(self):
        print(self.__balance)
obj=BankAccount(1000)
obj.deposit(1000)
obj.withdraw(200)
obj.show()
print()