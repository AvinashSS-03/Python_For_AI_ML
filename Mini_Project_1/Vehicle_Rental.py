'''
Project: Vehicle Rental System

Problem Statement
You are building a small program for a vehicle rental company.

 Requirements
Create a base  class Vehicle with attributes:brand model And a method show_details() that prints them.

Create a child class Car that inherits from Vehicle.
Extra attribute: seating_capacity
Method rental_price(days) → calculates rental price as days * 1000.
Override show_details() to display seating capacity too.

Create another child class Bike that inherits from Vehicle.
Extra attribute: engine_cc
Method rental_price(days) → calculates rental price as days * 500.
Override show_details() to display engine CC.

Create objects for both Car and Bike, display their details, and calculate rental price for a given number of days.
'''
class vehicle:
    def __init__(self,brand, model):
         self.brand=brand
         self.model=model
    def show(self):
        print("The vehicle Brand",self.brand)
        print("The Model",self.model)

class  car(vehicle):
     def __init__(self,seating_capacity,brand,model):
         super().__init__(brand,model)
         self.seating_capacity=seating_capacity


     def rental_price(self,days):
         return days*1000

     def show(self):
         super().show()
         print("The seating capacity of the vehicle is", self.seating_capacity)





class bike(vehicle):
    def __init__(self,engine_cc,brand,model):
        super().__init__(brand,model)
        self.engine_cc=engine_cc

    def rental_price(self, days):
        n = days * 500
        return n
    def show(self):
        super().show()
        print("The engine capacity is: ",self.engine_cc)


print("Welcome to the Vehicle Rental System")
print("Choose the option between 1 and 2")
print("Choose 1 if you need to rent a car")
print("Choose 2 if you need to rent a bike")
n=int(input("Please choose between 1 and 2 :"))
d=int(input("number of days you need for rent: "))

#car
if n==1:
    ca=car(12,"Maruti","Dizire")
    ca.show()
    print("The total rent is: ",ca.rental_price(d))

elif n==2:
#bike
    bi=bike(110,"BMW","GS100")
    bi.show()
    print("The total rent for the bike is: ",bi.rental_price(d))


else:
    print("Enter a valid number")
















