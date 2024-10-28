#Loop examples

#program runs only if user says yes
userChoice = input("Wanna run the program? ").lower()

while userChoice == "yes":
    print("^:^" * 10)
    print("program is running")
    print()
    userChoice = input("Run Againg? ").lower()


# Loop break
print("Thanks for using the program, bye!!")


# Numeric varible to control loop
controller = 0
max_vaule = int(input("Enter max vaule: "))
while controller <= max_vaule:
    #add one to controller
    print(controller)
    controller += 1
#Loop breaks
print(f"Loop broke bc controller hit max vuale")
print("controller is", controller)
