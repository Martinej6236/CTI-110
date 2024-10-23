# Jonathan Martinez
# 10/14/2024
# P3LAB
# Calculate the most efficient change as coins

'''# Regular division
print(100/3)

#floor diision - returns interger portion with the remainder
print(100//3)

#Modulo - reuturns ONLY the remainder
print(100%3)
print(7%4)
'''
# Get amount of money from user as float
money = float(input("Enter the amount of money as a float: $"))

#Convert money into a whole number
money = round(money * 100)

if money ==0:
    print("No change")
#May need to round this vaule
#money = round(money * 100)


#get whole dollars from money amount
dollars = money // 100
#print(f"Dollars: {dollars}")
#remove the dollar amount from money
money = money - (dollars * 100)

#get quarters from money amount
quarters = money // 25
#print(f"Quarters: {quarters}")
#remove the quarters amount from money
money = money - (quarters * 25)

#get dimes from money amount
dimes = money // 10
#print(f"Dimes: {dimes}")
#remove the dimes amount from money
money = money - (dimes * 10)

#get Nickles from money amount
Nickles = money // 5
#print(f"Nickles: {Nickles}")
#remove the quarters amount from money
money = money - (Nickles * 5)


#get pennies from money amount
pennies = money 
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
    if Nickles== 1:
        print(f"{pennies} penny")
    else: #More than one penny
             print(f"{pennies} pennies")             

