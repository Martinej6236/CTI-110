# Jonathan Martinez
# 10/23/2024
# P3HW2
# Claculate reg amd OT pay for an employee
'''
input: get name from user as a string
input: get numbers of hours worked as an interger
input: get reg pay rate as float
output a dotted line and the employee name
if the employee has overtime (hours worked > 40)
calculate OT hours (hours worked - 40)
calculate OT pay rate (reg pay rate * 1.5)
determine reg hours worked - has to be 40
calculate pay for regular hours (40 * reg pay rate)
calculate OT pay (OT hours * OT pay rate)
calculate gross pay (reg pay + OT pay)
else (has no overtime)
hours worked is original vaule from the beggining
pay rate is same from beggining
OT hours is 0
OT pay rate is 0
calculate pay for reg hours (hours worked * 40)
'''
# Get employee information for hours and pay
name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Print the employee name
print("-" * 50)
print(f"Employee name: {name}")
print()

#variables for output(also to remember them)
reg_hours = 0
ot_hours = 0
ot_pay_rate = 0
reg_pay = 0
ot_pay = 0

# Calculate pay based on whether overtime hours happend
if hours_worked > 40:
    # Has overtime
    reg_hours = 40
    ot_hours = hours_worked - 40
    ot_pay_rate = pay_rate * 1.5
    reg_pay = reg_hours * pay_rate
    ot_pay = ot_hours * ot_pay_rate
else:
    # No overtime 
    reg_hours = hours_worked
    reg_pay = hours_worked * pay_rate
    
# Calculate gross pay
gross_pay = reg_pay + ot_pay

# Display employees information and results and pay
print("Hours Worked   Pay Rate    OverTime    OverTime Pay     RegHour Pay     Gross Pay")
print("-" * 85)
print(f"{hours_worked:<14.1f}{pay_rate:<12.2f}{ot_hours:<12.1f}${ot_pay:<14.2f}${reg_pay:<14.2f}${gross_pay:.2f}")
