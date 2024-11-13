# Jonathan Martinez
# 11/13/2024
# P5Lab
# Simulate self-checkout using functions

# import random libary to use in program
import random


def disperse_change(change):
    print()
    print(f"Change owed: {change:.2f}")
        #Convert money into a whole number
    change = int(round(change * 100, 2))

    

    if change ==0:
        print("No change")
    #May need to round this vaule
    #money = round(money * 100)


    #get whole dollars from money amount
    dollars = change // 100
    #print(f"Dollars: {dollars}")
    #remove the dollar amount from money
    change = change - (dollars * 100)

    #get quarters from money amount
    quarters = change // 25
    #print(f"Quarters: {quarters}")
    #remove the quarters amount from money
    change = change - (quarters * 25)

    #get dimes from money amount
    dimes = change // 10
    #print(f"Dimes: {dimes}")
    #remove the dimes amount from money
    change = change - (dimes * 10)

    #get Nickles from money amount
    Nickles = change // 5
    #print(f"Nickles: {Nickles}")
    #remove the quarters amount from money
    change = change - (Nickles * 5)


    #get pennies from money amount
    pennies = change 
    #print(f"Pennies: {pennies}")

    #Display number of dollars and coins
    if dollars >= 1:
        if dollars== 1:
            print(f"{dollars} dollar")
        else: #More than one dollar
                 print(f"{dollars} dollars")

    if quarters >= 1:
        if quarters== 1:
            print(f"{quarters} quarter")
        else: #More than one quarter
                 print(f"{quarters} quarters")

    if Nickles >= 1:
        if Nickles== 1:
            print(f"{Nickles} nickle")
        else: #More than one nickle
                 print(f"{Nickles} nickles")

    if dimes >= 1:
        if dimes== 1:
            print(f"{dimes} dime")
        else: #More than one dime
                 print(f"{dimes} dimes")

    if pennies >= 1:
        if pennies== 1:
            print(f"{pennies} penny")
        else: #More than one penny
                 print(f"{pennies} pennies")
                
    



    

# Define the main function
def main():
    print("Welcome to the store!")
    # Generate money owed
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed:.2f}")
    inPut = float(input("How much cash will you put in the self check-out? $"))
    change = inPut - owed
    change = round(change, 2)
  

    # call the function to show the change as coins
    disperse_change(change)

    

# call the main
if __name__ == "__main__":
    main()
