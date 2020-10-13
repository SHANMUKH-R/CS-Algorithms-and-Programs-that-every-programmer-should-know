#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle
side_1=int(input("Enter the length of first side:"))
side_2=int(input("Enter the length of second side:"))
side_3=int(input("Enter the length of third side:"))
if(side_1==side_2==side_3):
    print("The triangle is equilateral triangle")
elif(side_1!=side_2!=side_3):
    print("The triangle is scalene triangle")
else:
    print("The triangle is isoceles triangle")