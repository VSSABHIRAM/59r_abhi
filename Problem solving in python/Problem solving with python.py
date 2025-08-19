# Week 1: Topics - Conditional statements, For and while  

# 1. If else and if else ladder 

# a. Easy Questions:

# i) Write a program to check if a given number is positive, negative, or zero.

def check_num(num1):
    if num1 > 0:
        return "positive"
    elif num1 < 0:
        return "negative"
    else:
        return "Zero"
    
res = float(input("Enter the number: "))
result = check_num(res)

print(result)

# ii) Determine if a number is odd or even.

def odd_even(num1):
    return 'even' if num1 % 2 == 0 else 'odd'

res = float(input("Enter the number: "))
result = odd_even(res)

print(result)

# iii) Check if a person is eligible to vote (age >= 18).

def vote_check(age):
    if age >= 18:
        return 'Eligible'
    else:
        return 'Not eligible'
    
res = int(input("enter your age: "))
result = vote_check(res)

print(result)

# iv) Write a program to find the greatest of two numbers.

def find_greastest(num1, num2):
    if num1 > num2:
        return f'{num1} is the greatest number'
    else:
        return f'{num2} is the greatest number'
    
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

result = find_greastest(num1, num2)
print(result)

# v) Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail."

def stud_mark(mark):
    if mark > 40:
        return 'pass'
    else:
        return 'fail'
    
mark = int(input("enter your marks: "))
result = stud_mark(mark)
print(result)

# vi. Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).

def num_to_week(num1):
    if num1 == 1:
        return 'monday'
    elif num1 == 2:
        return 'tuesday'
    elif num1 == 3:
        return 'wednesday'
    elif num1 == 4:
        return 'thursday'
    elif num1 == 5:
        return 'friday'
    elif num1 == 6:
        return 'saturday'
    elif num1 == 7:
        return 'sunday'
    else:
        return 'Invalid number'
    
res = int(input("enter the number: "))
result = num_to_week(res)
print(result)

# vii) Implement a simple calculator to perform addition, subtraction, multiplication, and division.

def simp_calc(op, a, b):
    if op in ['+', 'add']:
        return a + b
    elif op in ['-', 'sub']:
        return a - b
    elif op in ['x', 'mult']:
        return a * b
    elif op in ['/', 'div']:        
        return a / b if b != 0 else print('invalid denominator')
    else:
        return ' invalid operator'
    
op = input('enter the operator: ').lower()
a = int(input('enter the 1st operand: '))
b = int(input('enter the 2nd operand: '))

result = simp_calc(op, a, b)
print(result)

# viii) Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).

def num_to_month(num1):
    if num1 == 1:
        return 'january'
    elif num1 == 2:
        return 'february'
    elif num1 == 3:
        return 'march'
    elif num1 == 4:
        return 'april'
    elif num1 == 5:
        return 'may'
    elif num1 == 6:
        return 'june'
    elif num1 == 7:
        return 'july'
    elif num1 == 8:
        return 'august'
    elif num1 == 9:
        return 'september'
    elif num1 == 10:
        return 'october'
    elif num1 == 11:
        return 'november'
    elif num1 == 12:
        return 'december'
    else:
        return 'Invalid number'
    
res = int(input("enter the number: "))
result = num_to_month(res)
print(result)

# b. Medium Questions: 
# i. Write a program to find the greatest of three numbers.

def great_num(a, b, c):
    if a > b and a > c:
        return f'{a} is the greatest number'
    elif b > a and b > c:
        return f'{b} is the greatest number'
    else:
        return f'{c} is the greatest number'
    
a = int(input('enter the 1st number: '))
b = int(input('enter the 2nd number: '))
c = int(input('enter the 3rd number: '))

result = great_num(a, b, c)
print(result)

# ii. Check if a year is a leap year.

def check_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return f'{year} is a leap year'
    else:
        return f'{year} is a not leap year'
    
num1 = int(input('enter the year: '))
result = check_leap_year(num1)
print(result)

# iii. Write a program to classify a character entered by the user as a vowel, consonant, or neither.

def check_letter(letter):
    if letter in ['a', 'e', 'i', 'o', 'u']:
        return f'{letter} is a vowel'
    elif 'a' <= letter <= 'z':
        return f'{letter} is a consonant'       
    else:
        return 'neither'
    
letter = input('enter the character: ').lower()
result = check_letter(letter)
print(result)

# iv. Calculate the grade of a student based on the marks they score: 1. 90-100 : Grade A 2. 80-89 : Grade B 3. 70-79 : Grade C 4. <70 : Fail. v. Write a program

def mark_to_grade(marks):
    if marks in range(90,101):
        return 'Grade A'
    elif marks in range(80,90):
        return 'Grade B'
    elif marks in range(70,79):
        return 'Grade C'
    elif marks in range(0,70):
        return 'Fail'
    else:
        'Invalid Marks'

score = int(input('enter your scpre: '))
result = mark_to_grade(score)
print(result)

#  v. Write a program to check if three sides length form a valid triangle.

def check_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return 'Valid Triangle'
    else:
        return 'Invalid Triangle'
    
a = int(input('enter the 1st side: '))
b = int(input('enter the 2nd side: '))
c = int(input('enter the 3rd side: '))

result = check_triangle(a, b, c)
print(result)