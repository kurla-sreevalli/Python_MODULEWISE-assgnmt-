#1)	What is the value of x
# a)	101
# b)	99
# c)	None of the above, this is an infinite loop
# d)	100

x = 0
while (x < 100):
  x+=2
print(x)

#2)	Using while loop accept numbers until the sum of number is less than 100.

# Sum of natural numbers up to num

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
   
#3)	Take 10 integers from keyboard using loop and print their average value on the screen

num = int(input('How many numbers: '))
total_sum = 0
	
for n in range(num):
	    numbers = float(input('Enter number : '))
	    total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)

#4)	Print the following patterns using loop :
"""
a.
*
**
***
****
"""

rows = 4
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")
"""
b.
   *  
 *** 
*****
 *** 
   *
"""

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

"""
c.
1010101
 10101 
  101  
   1   
"""

rows = 3

k = 2 * rows - 2

for i in range(rows, -1, -1):

    for j in range(k, 0, -1):

        print(end=" ")

    k = k + 1

    for j in range(0, i + 1):

        print("1", end=" ")

    print("")


#5)	Print multiplication table of given number
# For example num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
    output = num,"X",i,
    output_mul= num * i
    print(output_mul)

#6)	Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# Expected output:
# 15
# 55
# 75
# 150

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)

#7)Given a number count the total number of digits in a number
#For example, the number is 75869, so the output should be 5.

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)

#8)Display -10 to -1 using for loop
# Expected output:
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(-10, 0):
    print(i)

#9)Display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.
# for i in range(5):
#     print(i)
# Expected output should be:
# 0
# 1
# 2
# 3
# 4
# Done!

for i in range(5):
    print(i)
else:
    print("Done!")


#10) Print the following pattern using nested for loop
"""
Expected output

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()




