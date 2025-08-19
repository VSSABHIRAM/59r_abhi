# Write a program to check the three sides will form a valid triangle and also check wheather the triangle is isosceles or equivalent or right angled.

def check_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print("Valid Triangle")
        
        # Type of triangle
        if a == b == c:
            print("Equilateral Triangle")
        elif a == b or b == c or c == a:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
        
        # Check for right-angled
        sides = sorted([a, b, c])   # sort the sides
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            print("Right-angled Triangle")
    else:
        print("Invalid Triangle")


a = int(input('enter the 1st side: '))
b = int(input('enter the 2nd side: '))
c = int(input('enter the 3rd side: '))

check_triangle(a, b, c)
