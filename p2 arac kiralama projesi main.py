# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:03:52 2024

@author: ASAF
"""

from p2arackiralamaprojesi import BikeRent, CarRent, Customer 

# Initialize the main menu flag
main_menu = True

# Create instances of BikeRent, CarRent, and Customer classes
bike = BikeRent(100)
car = CarRent(100)
customer = Customer()

# Main loop for the vehicle rental shop
while True:
    if main_menu:
        # Display the main menu options
        print("""
              *****  Vehicle rental shop  *****
              A : Bike Menu
              B : Car Menu
              Q : Quit
              
              """)
        main_menu = False
        
        # Get the user's choice
        choice = input("Enter Choice : ")
        
    if choice == "a" or choice == "A":
        # Display the bike menu
        print("""
              *****  Bike Menu  *****
              1. Display available bikes
              2. Request a bike hourly (5 $)
              3. Request a bike daily (84 $)
              4. Return a bike
              5. Main menu
              6. Exit
              """)
        
        choice = input("Enter choice :")
        
        try:
            choice = int(choice)
        except ValueError:
            print("it is not an integer")
            continue
        
        if choice == 1:
            # Display the available bikes
            bike.displayStock()

        elif choice == 2:
            # Request a bike rental on an hourly basis
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("---------------------")
        elif choice == 3:
            # Request a bike rental on a daily basis
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("---------------------")
        elif choice == 4:
            # Return a bike
            customer.bill = bike.returnVeichle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0, 0, 0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            # Exit the program
            break
        else:
            print("Invalid input. Please enter a number between 1-6")
            main_menu = True
   
    if choice == "b" or choice == "B":
        # Display the car menu
        print("""
              *****  Car Menu  *****
              1. Display available cars
              2. Request a car hourly (10 $)
              3. Request a car daily (168 $)
              4. Return a car
              5. Main menu
              6. Exit
              """)
        
        choice = input("Enter choice :")
        
        try:
            choice = int(choice)
        except ValueError:
            print("it is not an integer")
            continue
        
        if choice == 1:
            # Display the available cars
            car.displayStock()

        elif choice == 2:
            # Request a car rental on an hourly basis
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("---------------------")
        elif choice == 3:
            # Request a car rental on a daily basis
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("---------------------")
        elif choice == 4:
            # Return a car
            customer.bill = car.returnVeichle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.car = 0, 0, 0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            # Exit the program
            break
        else:
            print("Invalid input. Please enter a number between 1-6")
            main_menu = True    
    
    elif choice == "Q" or choice == "q":
        # Exit the program
        break   

    else:
        print("Invalid input. Please enter A-B-Q")
        main_menu = True
    print("Thank you for using the vehicle rental shop")  