 #Jonathan
 #9/16/2024
 #P1WH1
 #Using math expressions with user input

print("------Calculation Exponents------")

base_vaule = input("Enter an integer as the base vaule: ")
 #Convert base_vaule to integer
base_vaule = int(base_vaule)

 #Get input from user and convert to interger
exponent = int(input("Enter an integer as the exponent: "))
               
 #Display math result to the user
print(base_vaule, "raised to the power of", exponent, "is", base_vaule**exponent)
print()
print("------Addition and Subtraction------")

starting_integer = input("Enter a starting integer: ")
 #convert starting_integer to an integer
starting_integer = int(starting_integer)
 #Get input from user to add
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))
 #Display addition and subtraction
print(starting_integer, "+", add, "-", subtract, "is equal to", starting_integer+add-subtract) 
