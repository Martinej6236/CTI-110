# Jonathan Martinez
# P4LAB2
# 10/30/2024
# Use a for loop and a qhile loop to display postive multiplacations tables


# Create a variable t make the program run the first time
run_again = "yes"

# While loop to control entire program
while run_again == "yes" :
    # Get input from user
    userNum = int(input("Enter an interger: "))
    #Check if userNum is postive
    if userNum >= 0:
        # Loop to print multiplications
        for num in range(1,13):
            print(f" {userNum} * {num} = {userNum*num}")
           
            
        # If userNum is negative tell user
        else:
            print("Program does not handle negative numbers!!")
    print("Program runs....")
    print()
    run_again = input("Would you like to run the program againg(yes/no)? ").lower()

# Loop breaks
print("Exiting program....")
