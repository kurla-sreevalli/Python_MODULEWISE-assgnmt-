#1 1) Select the right way to create a string literal Ault'Kelly
# a)	  str1 = ‘Ault\\’Kelly’
# b)	  str1 = ‘Ault\’Kelly’
# c)	  str1 = “””Ault’Kelly”””

str1 = ‘Ault\\’Kelly’
str1 = ‘Ault\’Kelly’
str1 = """Ault’Kelly"""
str1 = "Ault'Kelly"
print(str1)
#2 2) In Python 3, what is the type of type(range(5))
# a)	  int
# b)	  list
# c)	  range

type(range(5)) #range
type(type(range(5))) #type
#3 3)  What is the data type of the following:

# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))

# a)	  list
# b)	  complex
# c)	  tuple

aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3])) #tuple
#4 4) Select all the valid String creation in Python
# a)	  str1 = “str1”
# b)	  str1 = ‘str1’
# c)	  str1 = ”’str1”’
# d)	  str1 = str(“str1”)

str1 = "str1"
str1 = ‘str1’
str1 = ”’str1”’
str1 = str(“str1”)
#5 5) What is the data type of print(type(10))
# a)	  float
# b)	  integer
# c)	  int

print(type(10))
#6 6)  What is the output of the following code
# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# a)	  False True False True
# b)	  True True False True
# c)	  True True False True
# d)	  False True True True

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
#7 7) What is the result of print(type([]) is list)
# a)	  False
# b)	  True

print(type([]) is list)
#8 
# 8)  What is the output of the following code?
# p, q, r = 10, 20 ,30print(p, q, r)
# a)	  10 20
# b)	  10 20 30
# c)	  Error: invalid syntax

p, q, r = 10, 20 ,30 
print(p, q, r)
#9 9) A string is immutable in Python?
# Every time when we modify the string, Python Always create a new String and assign a new string to that variable.

# a)	  True
# b)	  False

"""string is immutable"""
#10 10) Identify the following Datatypes:
# a)	“EXCELR” 
# b)	[1,2.3,”apple”] 
# c)	(1,2.3,”apple”)
# d)	15 
# e)	15.78 
# f)	True & False 

type("EXCELR")
type([1,2.3,"apple"])
type((1,2.3,"apple"))
type(15) 
type(15.78) 
type(True & False)
