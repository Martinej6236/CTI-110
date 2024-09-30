 # Jonathan Martinez
 # 9/30/2024
 # P2LAB1
 # Using imported libary, math, and f-string

 #Import math libary
import math

 #Get the radius from the user
radius = float (input("what is the radius of the circle? "))
print()

 # Calculate diameter
diameter = 2 * radius

 # Display diamter with one decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")

 #Calculate circumference
circum = 2 * math.pi * radius

 #Display the circumfrence with two decimal places
print(f"The circumference of the circle is {circum:.2f}\n")

 #Calculate the area
area = math.pi * (radius ** 2)

#Display area
print(f"The area of the circle is {area:.3f} \n")
    
