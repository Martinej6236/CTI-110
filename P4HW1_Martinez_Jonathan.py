# Jonathan Martinez
# 11/4/2024
# P4HW1
# Get scores using loop and a list

userNum = int(input("How many scores do you want to enter? "))
validScore = []

# For loop to allow user to enter scores
for grade in range(0, userNum):
    userInput = float(input(f"Enter score #{grade+1}: "))
    
    # Validate the score
    while userInput < 0 or userInput > 100:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        userInput = float(input(f"Enter score #{grade+1} again: "))
    
    # Add valid score to list
    validScore.append(userInput)

# Find lowest score manually
lowest_score = validScore[0]
lowest_index = 0
for i in range(1, userNum):
    if validScore[i] < lowest_score:
        lowest_score = validScore[i]
        lowest_index = i

# Remove lowest score manually
new_scores = []
for i in range(userNum):
    if i != lowest_index:
        new_scores.append(validScore[i])
validScore = new_scores

# Calculate sum manually
total = 0
count = 0
for score in validScore:
    total += score
    count += 1

# Calculate average
average = total / count


# Determine letter grade
if average >= 90:
    letter = 'A'
elif average >= 80:
    letter = 'B'
elif average >= 70:
    letter = 'C'
elif average >= 60:
    letter = 'D'
else:
    letter = 'F'

# Display results
print()
print('--------------------Results----------------------')
print(f'Lowest Score  : {lowest_score}')
print(f'Modified List : {validScore}')
print(f'Scores Average: {average:.2f}')
print(f'Grade        : {letter}')
print('-----------------------------------------------')
