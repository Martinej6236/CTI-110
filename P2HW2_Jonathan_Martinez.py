 #Jonathan Martinez

 #10/9/2024

 #P2HW2

 #using lists in python

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
print("--------Results--------")
print(f"{'Lowest Grade:':<25} ", min(my_list))
print(f"{'Higest Grade:':<25} ", max(my_list))
print(f"{'Sum of Grades:':<25} ", sum(my_list))
print(f"{'Avergage:':<26} {Avg:.2f}")

