# Learning to use user-defined funcions

# define a multiply function
def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)

# define add  function
def add(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)

def returnNum():
    userInput = input("Give me a big number: ")
    while not userInput.isnumeric():
       print("Vaule must be a number")
       userInput = input("Give me a big number: ")
    return int(userInput)

def getName(lastName):
    name = input("Enter your first name: ")
    fullname = "*******" + name + "***************" + lastName
    return fullname 
    

# Define Function
def main():
    # Get input from user
    first_num = int(input("Gimme a number"))
    second_num = int(input("Gimme a number"))
    third_num = int(input("Gimme a number"))

#call the multiply function
    multiply(first_num, second_num, third_num)

# call the add function
    add(first_num, second_num, third_num)

#Call the vaule returning
    bigNum = returnNum()

    print(bigNum * 5)

    print(getName("Milstead"))

# Call the main function
if __name__== "__main__":
    main()