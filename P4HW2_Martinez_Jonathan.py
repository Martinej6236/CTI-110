# Jonathan Martinez
# 11/4/2024
# P4HW2
# Program calculates employee pay including overtime and keeps running totals

# Create variables to hold running totals
numEmployees = 0
overtimeTotal = 0
regPayTotal = 0
grossPayTotal = 0

# Get first employee name
employeeName = input('Enter employee name or "Done" to terminate: ').capitalize()

# Loop to control the main program
while employeeName.lower() != "done":
    numEmployees += 1
    
    # Get hours and pay rate
    hours = float(input(f"How many hours did {employeeName} work? "))
    payRate = float(input(f"What is {employeeName}'s pay rate? "))
    
    # Calculate overtime and regular hours
    if hours > 40:
        overtimeHours = hours - 40
        regularHours = 40
    else:
        overtimeHours = 0
        regularHours = hours
    
    # Calculate pay
    regularPay = regularHours * payRate
    overtimePay = overtimeHours * (payRate * 1.5)
    grossPay = regularPay + overtimePay
    
    # Add to running totals
    overtimeTotal += overtimePay
    regPayTotal += regularPay
    grossPayTotal += grossPay
    
    # Display individual results
    print()
    print('Employee name:', employeeName)
    print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
    print('--------------------------------------------------------------------------------')
    print(f'{hours:<14.1f}${payRate:<10.2f}{overtimeHours:<11.1f}${overtimePay:<13.2f}${regularPay:<12.2f}${grossPay:.2f}')
  
    
    # Get next employee name
    print()
    employeeName = input('Enter employee name or "Done" to terminate: ').capitalize()

# Display final totals after loop breaks
print()
print(f'Total number of employees entered: {numEmployees}')
print(f'Total amount paid for overtime: ${overtimeTotal:.2f}')
print(f'Total amount paid for regular hours: ${regPayTotal:.2f}')
print(f'Total amount paid in gross: ${grossPayTotal:.2f}')

