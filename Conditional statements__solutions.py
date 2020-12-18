#1 What is the output of the following if statement
a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')


#2 Given the nested if-else structure below, what will be the value of x after code execution completes
x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

#3 Given the nested if-else below, what will be the value x when the code executed successfully
x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

#4 A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = input("enter marks:")
marks = int(marks)
if marks <25:
    print("F")
elif marks>=25 and marks<45:
    print("E")
elif marks>=45 and marks<50:
    print("D")
elif marks>=50 and marks<60:
    print("C")
elif marks>=60 and marks<80:
    print("B")
else:
    print("A")

#5)	A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = input("enter quantity:")
quantity = int(quantity)
if quantity*100>1000:
    print("cost is:",((quantity*100)-(0.1*quantity*100)))
else:
    print("cost is:",quantity*100)

#6)	Write a program to print absolute value of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

print("enter a number:")
number = input()
number = int(number)
if number<0:
    print(number*-1)
else:
    print(number)

#7)	Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

str = input("Input a string: ")
d=l=0
for c in str:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

#8)	Write a Python program to check whether an alphabet is a vowel or consonant. 
# Expected Output:
# Input a letter of the alphabet: k                                       
# k is a consonant.

l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 
	
#9)	Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle 

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")

#10)	Write an If elif else condition for finding the largest number in 3 numbers.

# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)







