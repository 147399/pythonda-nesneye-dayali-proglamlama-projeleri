# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:12:06 2024

@author: ASAF
"""

import datetime

class VehicleRent:
    """
    Parent class for vehicle rental.
    """

    def __init__(self, stock):
        """
        Initialize the VehicleRent object with the given stock value.
        """
        self.stock = stock
        self.now = 0
        

    def displayStock(self):
        """
        Display the current stock of vehicles.
        """
        print("{} vehicles available for rent".format(self.stock))
        return self.stock

    def rentHourly(self, n):
        """
        Rent vehicles on an hourly basis.
        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicles available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle(s) for hourly at {} hours".format(n, self.now.hour))
            self.stock -= n
            return self.now

    def rentDaily(self, n):
        """
        Rent vehicles on a daily basis.
        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicles available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicles for daily at {} hours".format(n, self.now.hour))
            self.stock -= n
            return self.now
    
    def returnVeichle(self , reguest , brand  ):
        
        """
 Return the bill for the rented vehicle.
 
 :param request: A tuple containing the rental time, rental basis, and number of vehicles.
 :param brand: The type of vehicle being returned.
 :return: The bill for the returned vehicle.
 """      
        car_h_price = 10
        car_d_price = car_h_price*7/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        
        
        rentalTime , rentalBasis , numOfVehicle = reguest
        bill = 0 
       
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle :
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
               
                if rentalBasis == 1 : # hourly 
                   bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                elif rentalBasis == 2 : # daily 
                   bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle                   
                if (2 <= numOfVehicle):
                   print("you have extra %20 discount ")
                   bill = bill *0.8
                
                print("thank you for returning your car ")
                print("price : {}$",format(bill))
                return bill
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle :
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
               
                if rentalBasis == 1 : # hourly 
                   bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                elif rentalBasis == 2 : # daily 
                   bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle                   
                if (2 <= numOfVehicle):
                   print("you have extra %20 discount ")
                   bill = bill *0.8
                
                print("thank you for returning your bike ")
                print("price : {}$",format(bill))
                return bill
        else :
            print("You do not a vehicle ")
            return None
# Child class for renting cars, inheriting from the VehicleRent parent class.
class CarRent(VehicleRent):
    
    global discount_rate  # Global variable for discount rate
    
    discount_rate = 15  # Discount rate for car rentals
    
    def __init__(self, stock):
        super().__init__( stock)  # Initialize CarRent class by calling parent class constructor
    
    def discount(self, b):
        """
        Calculate discount for car rental.

        :param b: The total bill before discount.
        :return: The bill after applying the discount.
        """
        bill = b - (b * discount_rate) / 100  # Calculate discounted bill
        return bill

# Second child class for renting bikes, also inheriting from the VehicleRent parent class.
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)  # Initialize BikeRent class by calling parent class constructor

# Customer class for handling customer requests and vehicle returns.
class Customer:
    
    def __init__(self):
        # Initialize customer attributes for bikes and cars
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    
    def requestVehicle(self, brand):
        """
        Request a vehicle for rental.

        :param brand: The brand of vehicle to rent (either "bike" or "car").
        :return: The number of requested vehicles.
        """
        if brand == "bike":
            # Get the number of bikes requested from the user
            bikes = input("How many bikes would you like to rent? ")
            try:
                bikes = int(bikes)  # Convert user input to integer
            except ValueError:
                print("Number should be a number")
                return -1
            
            if bikes < 1:
                print("Number of bikes should be greater than zero")
            else:
                self.bikes = bikes
            return self.bikes
        
        elif brand == "car":
            # Get the number of cars requested from the user
            car = input("How many cars would you like to rent? ")
            try:
                car = int(car)  # Convert user input to integer
            except ValueError:
                print("Number should be a number")
                return -1 
            
            if car < 1:
                print("Number of cars should be greater than zero")
            else:
                self.cars = car
            return self.cars
            
        else:
            print("Request vehicles error")
 
    def returnVehicle(self, brand):
        """
        Return a rented vehicle.

        :param brand: The brand of vehicle to return.
        :return: The rental time, rental basis, and number of vehicles returned.
        """
        if brand == "bikes":
            # Check if rental information for bikes is available and return it
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0, 0, 0 
            
        elif brand == "car":
            # Check if rental information for cars is available and return it
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0, 0, 0
            
        else:
            print("Return vehicle error")






