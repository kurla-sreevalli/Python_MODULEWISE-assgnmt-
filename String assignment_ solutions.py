"""
1) Which method/inbuilt function should I use to convert String
 "welcome to the beautiful world of python" 
 to
 "Welcome To The Beautiful World Of Python".
"""

string = "welcome to the beautiful world of python"
string.title()


#2) Split a given string on hyphens into several substrings
str1 = "Emma-is-a-data-scientist"
str1.split("-")


#3) Remove empty strings from a list of strings
"""
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:
Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']
"""
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

without_empty_strings = []
for string in str_list:
    if (string != ""):
        without_empty_strings.append(string)

print(without_empty_strings)


#4) Create an string and execute the following inbuilt functions on it.
#- upper, lower, capitalize, split, join, isnumeric, isalpha, isdigit, count, isalnum.

A_string = "Archie Andrews: A high school football player who has a passion for music. Team Bulldogs 10"
B_string = "He is best friends with Jughead Jones and Betty Cooper"
A_string.upper()
A_string.lower()
A_string.capitalize()
A_string.split(":")
"archie andrews".join("10")
A_string.isnumeric()
A_string.isalpha()
A_string.isdigit()
A_string.count("passion")

strng = "hello10"
strng.isalnum()


#5) Guess the correct output of the following code?
# str1 = "PYnative"
# print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
# a)	PYn PYnat ive PYnativ vitanYP
# b)	  Yna PYnat tive PYnativ vitanYP
# c)	  Yna PYnat tive PYnativ PYnativ

str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1]) #c


#6) write the correct output of the following String operations
str1 = 'Welcome'
print(str1*2) #WelcomeWelcome


#7) Find all occurrences of “USA” in given string ignoring the case
str1 = "Welcome to USA. USA awesome, isn't it?"
str1.count("USA")
#Outcome:
#The USA count is: 2




















