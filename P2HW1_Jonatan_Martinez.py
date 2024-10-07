 # Jonathan Martinez
 # 10/7/2024
 # P2HW1
 # This program calculates and displays travel expenses
print("This program calculates and displays travel expenses ")
print()
 #Get budget from user
Budget =int (input("Enter Budget: "))
print()
 #Get user travel location
Location =input("Enter your travel destination: ")
print()
 #Get user Gas expenses
Gas =int (input("How much do you think you will spend on gas? "))
print()
 #Get user Hotel expenses
Hotel =int (input("Approximately, how much will you need for accomodation/hotel?"))
print()
#Get user Food expenses
Food =int(input("Last, how much do you need for food? "))
print()
 #List expenses and use string 
print("-------Travel Expenses-------" )
print(f"{'Location:':<18}{Location:<25}")
print(f"{'Intitial Budget:':<18}"f"${Budget:<25,.2f}")
print(f"{'Fuel:':<18}"f"${Gas:<25,.2f}" )
print(f"{'Accomodation:':<18}"f"${Hotel:<25,.2f} ")
print(f"{'Food:':<18}"f"${Food:<25,.2f} ")
print("--------------------------------")
 #Calculate the remaining Balance
Balance = Budget - (Gas + Food + Hotel)
print()
print(f" Remaining Balance: ${Balance:.2f} " )
