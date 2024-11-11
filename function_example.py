# Learning to use user-defined funcions

# define a multiply function
def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)


# define a  function
def add(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)

# Define Function
Def main():
    # Get input from user
    first_num = int(input("Gimme a number"))
    second_num = int(input("Gimme a number"))
    third_num = int(input("Gimme a number"))


# call the add function
add(first_num, second_num, third_num)

# Call the main function
if __name__== "__main__":
    main()