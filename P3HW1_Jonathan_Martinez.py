 #Jonathan Martinez

 #10/14/2024

 #P3HW1

 #use brachning to get a letter grade

#Get grades for modules from user

my_list = []

Module_1 = float(input("Enter Grade for Module 1: "))
Module_2 = float(input("Enter Grade for Module 2: "))
Module_3 = float(input("Enter Grade for Module 3: "))
Module_4 = float(input("Enter Grade for Module 4: "))
Module_5 = float(input("Enter Grade for Module 5: "))
Module_6 = float(input("Enter Grade for Module 6: "))
print()
#Add varibles to list
my_list.append(Module_1)
my_list.append(Module_2)
my_list.append(Module_3)
my_list.append(Module_4)
my_list.append(Module_5)
my_list.append(Module_6)

Avg = sum(my_list) / len(my_list)
#Get the results
print("--------Results---------------------------")
print(f"{'Lowest Grade:':<25} ", min(my_list))
print(f"{'Higest Grade:':<25} ", max(my_list))
print(f"{'Sum of Grades:':<25} ", sum(my_list))
print(f"{'Avergage:':<26} {Avg:.2f}")
print("-------------------------------------------")
#Create grading if

if Avg >= 90:
    letter_grade ="A"
elif Avg >= 80:
    letter_grade ="B"    
elif Avg >= 70:
    letter_grade ="C"
elif Avg >= 60:
    letter_grade ="D"
else:
    letter_grade ="F"
#Dispay results
print(f"Your grade is: {letter_grade}")
