
#1) Select all the correct options to join two lists.
listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']
# a)	newList = listOne + listTwo
# b)	  newList = extend(listOne, listTwo)
# c)	  newList = listOne.extend(listTwo)
# d)	  newList.extend(listOne, listTwo)

print( listOne + listTwo)
listOne.extend(listTwo)
print(listOne)

#2) Create an list of elements and execute the following functions:
    #reverse, append, extend, count,sort.
listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'g', 'f']

listOne.reverse()
print(listOne)

listOne.append(50)
listOne

listOne.extend(listTwo)
listOne

listOne.count('a')

listTwo.sort()
listTwo

#3)  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Sample_List = [x for (i,x) in enumerate(Sample_List) if i not in (0,4,5)]
print(Sample_List)

#Expected_Output = ['Green', 'White', 'Black']

#4) What is the output of the following list operation
aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5]) #[30, 40, 50]
print(aList[:4]) #[10, 20, 30, 40]
print(aList[3:]) #[40, 50, 60, 70, 80]

#5) Select all the correct options to copy a list
aList = ['a', 'b', 'c', 'd']

# a)	newList = copy(aList)
# b)	  newList = aList.copy()
# c)	  newList.copy(aList)
# d)	  newList = list(aList)

newList = aList.copy()
newList

#6) Create an list of elements and slice & dice it.

clist=[34,5,45.4,"java","oracle","unix"]
print(clist[-3:-1])

#7) Given a Python list you should be able to display Python list in the following order

python_list = [100, 200, 300, 400, 500]
python_list.sort(reverse=True)
python_list
#Expected output:
[500, 400, 300, 200, 100]

#8) What will be the output of the following code snippet?
a=[1,2,3,4,5]
print(a[3:0:-1]) #[4, 3, 2]

#9) Add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
list1

#Expected output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
























