# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 03:34:11 2020

@author: sreevalli kurla ksv
"""

#1. Write a Python program to count the number of characters (character frequency) in a string

from collections import Counter
print(Counter('cats on wheels'))

#OR

word="Hello"
characters={}
for character in word:
    if character in characters:
        characters[character] += 1
    else:
        characters[character] =  1
print(characters)

#2. Write a Python program that takes a list of words and returns the length of the longest one

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["C", "Java","Python"]))

#3. Write a Python program to count the occurrences of each word in a provided sentence

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('python program to convert a list to string'))

#4. Write a Python program to count the vowels and display the vowels of a given text

def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])
vowel('Welcome to w3resource.com')

#5. Write a Python program to check a list is empty or not

list_a=[] # Empty lists evaluate to False
if len(list_a)==0:
    print ("list is empty")
else:
    print ("list is not empty")

#6. Write a Python program to remove duplicates from a list.

a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

#7. Write a Python program to capture any filename from the keyboard and display its filename and extension separately.

filename=input("enter any filename:")
print("you entered:",filename)
output=filename.split(".")
print(output)

print("filename:", output[0])
print("extension:", output[1])

#8. Write a Python program to capture some delimited string from the keyboard and split the string with a comma and display the length after splitting.

string = input("enter a string with delimeter:")
output = string.split(",")
print(output)
len(output)

#9. Write a Python program to capture 2 numbers from the keyboard and display its sum.

# Store input numbers
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# Add two numbers
sum = num1+num2

# Display the sum
print("sum:",sum)

#10. Write a Python program to find the second smallest number in a list.

def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([1, 2, -8, -2, 0, -2]))
# print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_smallest([2,2]))
# print(second_smallest([2]))

#11. Write a Python program to get the count of each element in a list.

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)

#12. Write a Python program to display all the UNIQUE elements of two lists and also COMMON elements of two lists.

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))

#13. Write a Python program to sort a tuple by its float element

#Sample data: [(‘item1’, ‘12.20’), (‘item2’, ‘15.10’), (‘item3’, ‘24.5’)]

price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))

#14. Write a Python program to convert a tuple to a dictionary

#create a tuple
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))

#15. Write a Python program to find the repeated items of a tuple

#create a tuple
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(tuplex)
#return the number of times it appears in the tuple.
count = tuplex.count(4)
print(count)

#16. Write a Python program to find maximum and the minimum value in a set

#Create a set
seta = set([5, 10, 3, 15, 2, 20])
#Find maximum value
print(max(seta))
#Find minimum value
print(min(seta))

#17. Write a Python Program to display all the UNIQUE elements of the list.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

#18. Write a Python program to create a dictionary from a string by counting the number of occurrences of each character.

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#19. Write a Python program to print all unique values in a dictionary.

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)

#20. Write a Python program to capture the string from the keyboard and reverse the string.

string = input("A String:")
print(string[::-1])

#21. Write a Python program to join two dictionaries

dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}
dict = dict1.copy()
dict.update(dict2)
print(dict)

#22. Write a Python program to capture any string from the keyboard and perform the below operations.

# check whether the string is upper or not
# convert the string to list
# display the string exactly in the center of 30 spaces width
# convert the string into lower case
# check whether ‘python’ is existing in the string or not

A_STRING= input("enter any string:")
A_STRING.isupper()
list(A_STRING)
A_STRING.center(30)
A_STRING.lower()
A_STRING.find("HELL")

#23. Define some tuple as below

# alist = (“unix”,”hadoop”,”oracle”,”scala”)

# Write a Python program to append “spark” to the tuple

A_tuple = ('unix','hadoop','oracle','scala')
conv_tuple=list(A_tuple)
conv_tuple.append("python")
A_tuple_output= tuple(conv_tuple)
print(A_tuple_output)

#24. Write a Python program to capture filename from the keyboard and display the type of the file

# if the filename is ending with .py …. display “Its python file”
# if the filename is ending with .pl …. display “Its perl file”
# If the filename is ending with .c … display “Its C lang file”
# if the filename is ending with .json … display “Its json file”:
    
FILEname= input("enter any file name:")
print("you entered:",FILEname)
if FILEname.endswith(".py"):
    print("Its python file")
elif FILEname.endswith(".pl"):
    print("Its perl file")
elif FILEname.endswith(".c"):
    print("Its C lang file")
elif FILEname.endswith(".json"):
    print("Its json file")
else:
    print("unknown format")

#25. Write a Python program to validate the IP address.

import socket
addr = '157.44.75.33'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")

#26. Write a Python program to capture any string from the keyboard and perform the below operation.

# if the string is defined in uppercase…… convert the string to lower and display it

# if the string is defined in lowercase …… convert the string to upper and display it.

string_1= input("enter any string:")
if string_1.isupper():
    print(string_1.lower())
elif string_1.islower():
    print(string_1.upper())
else:
    print("Invalid Format")

#27. Write a Python program to capture username and password from the keyboard and validate the password

# condition1: length of the password should be greater than 5
# condition2: length of the password should be less than 12
# condition3: atleast one symbol ( @ or * or $ ) should exist in the password
# condition4: whole password SHOULD not be in upper case

import re
U = input("Give an username:")
P = input("Input your password:")
x = True
while x:  
    if (len(P)<5 or len(P)>12):
        break
    elif not re.search("[a-z]",P):
        break
    #elif not re.search("[A-Z]",P):
        #break
    elif not re.search("[$*@]",P):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

#28. Write a Python program to count the number of even and odd numbers from the provided list.

alist = [ 56,34,23,56,4,43,6,7,5,34,5,7645,573,23,6,7,5,4,6,7,5634,3454,345,67,32,45]
Tup = tuple(alist)
print(Tup)
count_odd = 0
count_even = 0
for x in Tup:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#29. Write a Python program to generate the following pattern using a loop number

#1 22 333 4444 55555 666666 7777777 88888888 999999999

for i in range(10):
    print(str(i) * i)

#30. Write a Python program to check whether the key “emp2” is existing in the list or not

#adict = {“emp1”:[“raj”,28] ,”emp2″:[“ram”,34] ,”emp3″:[“rita”,24]}

adict={"chap1":10,"chap2":20,"chap3":30}
print(adict)
output= adict.get("chap6")
print(output)

#31. Write a Python program to count the no. of occurences of each item

data = ['perl','unix','perl','scala','perl']

from collections import Counter
print(Counter(data))

#32. Write a Python program for performing the below operation

# define empty tuple
# append “unix” to the tuple
# append few more elements like ‘spark’, ‘scala’ , ‘Hadoop’, ‘sccm’ to the list
# append few more elements like ‘c’,’cpp’,’java’,’salesforce’,’sap’,’unix’ to the list
# remove java
# remove salesforce –
# add ‘oracle’ at the index 0
# add ‘ mongodb’ at the index 5
# reverse all the elements
# display the total. no. of elements of the list
# display the total count of ‘unix’ in the list

tuple_new = tuple()

tup = list(tuple_new)
tup.append("unix")
tup

alist = ["saprk","scala","hadoop","sccm"]
tup.extend(alist)
tup

blist = ["c","cpp","java","salesforce","sap","unix"]
tup.extend(blist)
tup

tup.remove("java")
tup

tup.remove("salesforce")
tup

tup.insert(0,"oracle")
tup

tup.insert(5,"mongodb")
tup

tup.reverse()
tup

len(tup)

tup.count('unix')

#33. Write a Python program to check whether ‘python’ is existing in the ‘perl,unix,hadoop,scala,spark,ruby,go’ or not.

list_of_elements = ["perl","unix","hadoop","scala","spark","ruby","go"]
list_of_elements.count("python")

#34. Write a Python program to append ‘spark’ to the below tuple

alist = ("unix","hadoop","oracle","scala")
output=list(alist)
output
output.append("spark")
print(output)

#35. Write a Python program to capture 2 numbers from the keyboard and display its sum as below.

# Enter first number : 10
# Enter second number: 20

# Total : 30

# Store input numbers
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# Add two numbers
sum = num1+num2

# Display the sum
print("sum:",sum)

#36. Write a Python program to display all the numbers from 50 to 1

for i in range(50,0,-1):
    print(i)

#37. Write a Python program to display all the odd numbers from 20 to 10

for i in range(19,10,-2):
    print(i)

#38. Define some list as below

# alist = [“google”,”oracle”,”microsoft”]
# Output:
# http://www.google.com
# http://www/.oracle.com
# http://www.microsoft.com

alist = ["google","oracle","microsoft"]

for item in alist:
    otpt="http://www."+item+".com"
    print(otpt)

#39. Write a Python program to add “http://www” at the beginning and add “.com” at the end of the string

# Output:
# http://www.google.com
# http://www/.oracle.com
# http://www.microsoft.com

string = input("enter any string:")
otpt="http://www."+string+".com"
print(otpt)

#40. Define some list as below

# domains = [“google”,”www.unix”,”oracle.com”]

# Write a Python program to add “www” at the beginning if the string is not starting with “www” and “.com” at the end of each string if the string is not ending with “.com”


alist = ["google","oracle.com","www.unix"]

for item in alist:
    if item.startswith("www.") and  item.endswith(".com"):
         print("www."+item+".com")
    elif not item.startswith("www.") and not item.endswith(".com"):
        print("www."+item+".com")
        
#### ANOTHER TRY

alist = ["google","oracle.com","www.unix"]

for item in alist:
    if item.startswith("www."):
         print(item+".com")
    elif  item.endswith(".com"):
         print("www."+item)
    else:
        print("www."+item+".com")
       
#41. Write a Python program to display the below IP addresses

# 192.168.0.1
# 192.168.0.2
# 192.168.0.3
# ..
# ..
# 192.168.0.10

fixed="192.168.0."
for val in range(1,11):
    ip=fixed+str(val)
    print(ip)

#42. Write a Python program to display the below IP addresses

# 192.168.0.1
# 192.168.0.2
# 192.168.0.3
# ..
# ..
# 192.168.0.10
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# ..
# ..
# 192.168.1.10

fixed="192.168.0."
for val in range(1,11):
    ip=fixed+str(val)
    print(ip)
fixed = "192.168.1."
for val in range(1,11):
    ip=fixed+str(val)
    print(ip)

"""
43. Define dictionary as below

infodoc = { 2001: {“ap”:76} , 2002:{“tn”:75} , 2003:{“up”:90} }

Write a Python program to display the below output

Output:

state literacy rate

—————————–

ap 70
tn 75
up 90
"""

infodoc = {2001: {"ap":76} , 2002:{"tn":75} , 2003:{"up":90} }
values = infodoc.values()
print(values)
for item in values:
    print(item[0],item[1])

#44. Define some dictionary as below

# adict = {“emp1”:[“raj”,28] ,”emp2″:[“ram”,34] ,”emp3″:[“rita”,24]}

# Write a Python program to check whether the key “emp2” is existing in the list or not

adict = {"emp1":["raj",28] ,"emp2":["ram",34] ,"emp3":["rita",24]}
output = adict.get("emp2")
print(output)

#45. Define a list below

#   (structured data)
colors = [
   {
     "colors": "red",
     "values": "#f00"
   },
   {
     "colors": "green",
     "values": "#0f0"
   },
   {
     "colors": "blue",
     "values": "#00f"
   },
   {
     "colors": "cyan",
     "values": "#0ff"
   },
   {
     "colors": "magenta",
     "values": "#f0f"
   },
   {
     "colors": "yellow",
     "values": "#ff0"
   },
   {
     "colors": "black",
     "values": "#000"
     }]


for item in colors:
    print(item['colors'],(item['values']))


#46. Define a dictionary as below

####################### (UNSTRUCTURED DATA)

data = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image": {
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail": {
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

for key,value in data.items():
    if isinstance(value,str):
        print(key.ljust(30),":",values)
    elif isinstance(value,dict):
        for skey,svalue in value.items():
            ikey = key+(".")+skey
            print(ikey.ljust(30),":",svalue)


#47. Define dictionary as below

#Write a Python program to display all etag information from the dictionary


########   ASSIGNMENT DISCUSSION 


ytag = {
  "kind": "youtube#searchListResponse",
  "etag": "m2yskBQFythfE4irbTIeOgYYfBU",
  "nextPageToken": "CAUQAA",
  "regionCode": "KE",
  "pageInfo": {
    "totalResults": 4249,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "m2yskBQFythfE4irbTIeOgYYfBU",
      "id": {
        "kind": "youtube#channel",
        "channelId": "UCJowOS1R0FnhipXVqEnYU1A"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "m2yskBQFythfE4irbTIeOgYYfBU",
      "id": {
        "kind": "youtube#video",
        "videoId": "Eqa2nAAhHN0"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "m2yskBQFythfE4irbTIeOgYYfB",
      "id": {
        "kind": "youtube#video",
        "videoId": "IirngItQuVs"
      }
    }
  ]
}


for key in ytag:
    if key=="etag":
        print(ytag[key])
    elif isinstance(ytag[key],list):
        for skey in ytag[key]:
            print(skey['etag'])


#48. Create a dictionary as below
#write a program to display the below output:

# Regular (1001)
# Chocolate (1002)
# Blueberry (1003)
# Devil’s Food (1004)

dict_D = {
  "id": "0001",
  "type": "donut",
  "name": "Cake",
  "ppu": 0.55,
  "batters": {
    "batter": [
      {
        "id": "1001",
        "type": "Regular"
      },
      {
        "id": "1002",
        "type": "Chocolate"
      },
      {
        "id": "1003",
        "type": "Blueberry"
      },
      {
        "id": "1004",
        "type": "Devil's Food"
      }
    ]
  },
  "topping": [
    {
      "id": "5001",
      "type": "None"
    },
    {
      "id": "5002",
      "type": "Glazed"
    },
    {
      "id": "5005",
      "type": "Sugar"
    },
    {
      "id": "5007",
      "type": "Powdered Sugar"
    },
    {
      "id": "5006",
      "type": "Chocolate with Sprinkles"
    },
    {
      "id": "5003",
      "type": "Chocolate"
    },
    {
      "id": "5004",
      "type": "Maple"
    }
  ]
}


for key in dict_D:
    if key=="batters":
        print(dict_D[key])
        batter = dict_D[key].get('batter')
        print("batter=",batter)
        for item in batter:
            print(item['type'],'('+(item['id'])+')')
        
##########


#49. Write a Python program that accepts a string and calculate the number of upper case letters and lower case letters.       
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


#50. Write a Python program that checks whether a passed string is palindrome or not

def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('level')) 


#51. Create a library named as operations which contains 4 functions as
# Add() for addition,
# Sub() for subtraction,
# Mult() for multiplication and
# Div() for division.

# All functions should accept two parameters as the number and perform the operation.
#Write a Python program which calls all the functions from the operations library by accepting the parameters from the user.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
operation = input("Enter which operation you want to perform as Add() for addition,Sub() for subtraction,Mult() for multiplication andDiv() for division: ")

result = 0
if operation == 'Add()':
    result = num1 + num2
elif operation == 'Sub()':
    result = num1 - num2
elif operation == 'Mult()':
    result = num1 * num2
elif operation == 'Div()':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, operation , num2, ":", result)

#52. Write a Python program to accept 10 random numbers from the keyboard and append all the numbers to the list. Now create 3 user-defined functions named as filter(), map() and reduce() in it.

# write the logic for
# -map function which will calculate the square of each number in the list to the new list.
# -filter function should filter all the numbers which are odd.
# -reduce function should calculate the sum of all the numbers in the list.

nums =input("Ten random numbers:")
print(nums)
new_list = list(nums)
print(new_list)
a_list = []
list_nums = a_list.append(new_list)
print("Original list of integers:")
print(list_nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, list_nums))
print(square_nums)

# (OR)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

##____

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)

##____

import functools
from functools import reduce
num_list = [1,2,3,4,5,55,65,8]
sum = reduce(lambda x,y: x + y, num_list)
print(sum) 


#53. Write a Python program to rewrite the above program using builtin functions map() , filter() and reduce().

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

##____

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)

##____

import functools
from functools import reduce
num_list = [1,2,3,4,5,55,65,8]
sum = reduce(lambda x,y: x + y, num_list)
print(sum) 
