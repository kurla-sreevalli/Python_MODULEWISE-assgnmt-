#1. Write a Python program to read the file realestate.csv and display the file content line by line with proper error handling.

try:
    find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
    print(find.readlines())
    find.close()
except Exception as error:
     print("System defined error :", error)
     
#2. Write a Python program to read realestate.csv and display ONLY street and city columns.

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    output= newfile.split(",")
    print("street:", output[0])
    print("city:", output[1])
    print("----------------------------")

find.close()

#3. Write a Python program to read realestate.csv and display all the UNIQUE cities and the count of unique cities.

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
cityset= set()    
#processing the data
for getlines in find:
    getlines=getlines.strip()
    output = getlines.split(",")
    city = output[1]
    #adding each city to set to capture unique city
    cityset.add(city)

#display output
for city in cityset:
    print((city))
find.close()
# the count of unique cities
len(cityset)


#4. Write a Python program to read realestate.csv and display the count of an individual city.

import collections

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
city_dict=dict()
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    output= newfile.split(",")
    A= collections.Counter(output[1])
    print(A)
    # city=output[1]
    # print(city)
    
find.close()


#5. Write a Python program to read realestate.csv and replace all the lines containing SACRAMENTO with BANGALORE in the same file.

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    newfile=newfile.replace("SACRAMENTO","BANGALORE")
    output= newfile.split(",")
    print(output)
    
find.close()

#6. Write a Python program to read realestate.csv and display all the lines satisfying the below

#– type should be residential

#– price shouldbe greater than 100000

#– city should be either SACRAMENTO or RIO LINDA

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    output= newfile.split(",")
    print("city:", output[1])
    print("type:", output[7])
    print("price:", output[9])
    print("----------------------------")
find.close()

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    output= newfile.split(",")
    if (output[7]=="Residential" and int(output[9])>100000) and (output[1]=="SACRAMENTO" or output[1=="RIO LINDA"]):
        print(output[0:12])
                
find.close()
            
##### OR

import re

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    output= newfile.split(",")
    Type = output[7]
    Price = output[9]
    City = output[1]
X = True
while X:
    if ("Residential", output[7]):
        break
    elif not re.search(int(output[9]>100000)):
        break
    elif not re.search(["SACRAMENTO" or "RIO LINDA"], output[1]):
        break
    else:
        print("lines satisfying the above conditions")
        X = False
        break
if X:
    print("do not satisfy the conditions")
    
find.close()        


#7.  Write a Python program to read sales.csv and display all the different(distinct) payment modes

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\sales.csv","r")
payment_set= set()    
#processing the data
for getlines in find:
    getlines=getlines.strip()
    output = getlines.split(",")
    payment = output[3]
    #adding each city to set to capture unique city
    payment_set.add(payment)

#display output
for payment in payment_set :
    print(payment)
find.close()

#8. Write a Python program to read sales.csv and display the country name and the no. of states of each country.

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\sales.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    output= newfile.split(",")
    print("state:", output[6])
    print("country:", output[7])
    print("----------------------------")

find.close()

































































