# Jonathan Martinez
 # 10/2/2024
 # P2LAB2
 # write a program that creates a dictionary where the key and value pairs 

#Create a Dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
print()

#Print all keys in dictionary
print(cars.keys())
print()

#Get a car (Key) from user
userCar = input("Enter a vehicle to see it's mpg: ")
print()

#Display mp for the userCar
print(f"The {userCar} gets {cars[userCar]} mpg.")
print()

#Get Miles to drive from user
miles_to_drive = int(input(f"How many miles would you like to drive the {userCar}? "))
print()

#Calculate gallons of gas needed
gallons_needed = miles_to_drive/cars[userCar]

#Display Gallons of gas needed
print(f"{gallons_needed} gallon(s) of gas are needed to drive the {userCar} {miles_to_drive} miles. ")
