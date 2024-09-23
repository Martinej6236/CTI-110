 # Jonathan
 # 9/23/2024
 # P1HW2
 # This program calculates and displays travel expenses
print("This program calculates and displays travel expenses ")
 #Get budget from user
Budget =int (input("Enter Budget: "))
 #Get user travel location
Location =input("Enter your travel destination: ")
 #Get user Gas expenses
Gas =int (input("How much do you think you will spend on gas? "))
 #Get user Hotel expenses
Hotel =int (input("Approximately, how much will you need for accomodation/hotel? "))
 #Get user Food expenses
Food =int(input("Last, how much do you need for food? "))
print()
 #List expenses
print("-------Travel Expenses-------" )
print("Location: " f"{Location}" )
print("Intitial Budget: " f"{Budget}" )
print()
print("Fuel: " f"{Gas}" )
print("Accomodation: " f"{Hotel} ")
print("Food: " f"{Food} ")
print()
 #Calculate the remaining Balance
Balance = Budget - (Gas + Food + Hotel)
print(f" Remaining Budget: {Balance} " )
