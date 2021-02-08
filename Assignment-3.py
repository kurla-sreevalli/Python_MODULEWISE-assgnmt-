
#1. Write a Python program to display all the files and directories from the current directory.

import os
import sys
try:
    files = os.listdir()#by default it takes the local directory
    for file in files:
        print(file)
except Exception as err:
    print(err)
    print(sys.exc_info())


#2. Write a Python program to display all the files and directories from the C:\ or \usr\bin (if using Linux).

import os
import sys
try:
    files = os.listdir("C:\\Users\\")
    for file in files:
        print(file)
except Exception as err:
    print(err)
    print(sys.exc_info())

#3. Write a Python program to display ONLY .py that are existing in the current directory. 

import os
import sys
try:
    files = os.listdir()
    for file in files:
        if file.endswith(".py"):
            print(file)
except Exception as err:
    print(err)
    print(sys.exc_info())


#4.Write a Python program to display ONLY .py files and its size as below from the current directory with proper formatting.

import os
import sys
try:
    files = os.listdir()
    for file in files:
        if file.endswith(".py") and os.path.getsize(file) > 0:
            print(file.ljust(30) , os.path.getsize(file),"bytes")
except Exception as err:
    print(err)
    print(sys.exc_info())
    
#5. Write a Python program to display ONLY .py files and its size as below from the current directory with proper formatting.

import os
import sys
try:
    path = "D:\\projects\\"
    os.chdir(path)
    files = os.listdir()
    for file in files:
        if file.endswith(".py") and os.path.isfile(file) and  os.path.getsize(file) > 0:
            print(file.ljust(30) , os.path.getsize(file),"bytes")
except Exception as err:
    print(err)
    print(sys.exc_info())


#6. Write a Python program to display all the files other than .py files from the current directory.  

import os
import sys
try:
    files = os.listdir()
    for file in files:
        if not file.endswith(".py") and os.path.isfile(file) and os.path.getsize(file) > 0:
            print(file.ljust(30) , os.path.getsize(file),"bytes")
except Exception as err:
    print(err)
    print(sys.exc_info())


#7. Write a Python program to display all the files and folders separately and its count also.

import os
import sys
filelist = []
dirlist = []
try:
    files = os.listdir()
    for file in files:
        if os.path.isfile(file):
            filelist.append(file)
        elif os.path.isdir(file):
            dirlist.append(file)
    for file in filelist:
        print(file)
    print("Total files count :", len(filelist))
    print()
    for file in dirlist:
        print(file)            
    print("Total directories count :", len(dirlist))
except Exception as err:
    print(err)
    print(sys.exc_info())

#8. Write a Python program to revoke all the write, execute permissions ( the files should be only read ONLY) to the files present in the current directory.

#os and sys modules provide numerous tools to deal with filenames, paths, directories
import os
import sys
#System-specific parameters and functions
#This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
try:
    files = os.listdir()
    for file in files:
        print(file)
        os.chmod(file,444)
except Exception as err:
    print(err)
    print(sys.exc_info())


'''
9.
display the current user name
display current working directory
display Operating system name
display process id of your running program
display the current timestamp
display yesterday's date
display tomorrow's date
display all the environment variables that are existing
display the python executable path  ( just like ‘which python3’ in Linux )
'''    

import os
import time
import datetime
import sys
import platform #The platform module includes tools to see the platform's hardware, operating. system, and interpreter version information where the program is running
try:
    print(os.getlogin())
    print(os.getcwd())
    print(platform.platform())
    print(platform.node()) #This function returns a string that displays the information about the node basically the system's network name
    print(os.getpid())
    print(datetime.datetime.now())
    today = datetime.date.today()
    print('Today:', today)
    yesterday = today - datetime.timedelta(days=1)
    print('Yesterday:', yesterday)
    tomorrow = today + datetime.timedelta(days=1)
    print('Tomorrow:', tomorrow)
    # environment variables are loaded automatically when rebooted. like python can be executable in any cmd pmpt
    print(os.environ)#Environment variables is the set of key-value pairs for the current user environment.
    print(sys.executable)# the folder where Python is installed will be listed --- that folder name is the path to Python.
except Exception as err:
    print(err)
    print(sys.exc_info())

"""
10. Write a Python program to display the below information.
– disk utilization of C:\ ( total , used and free space)
– disk utilization of \tmp ( if using linux)
– display CPU utilization
– display Memory utilization
"""

import psutil
#python system and process utilities
#is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python
import os
#OS module in python provides functions for interacting with the operating system.
import shutil
#It is a utility module which can be used to accomplish tasks, such as: copying, moving, or removing directory trees.
try:
    print(shutil.disk_usage("C:\\"))
    print(psutil.cpu_percent())
    print(psutil.virtual_memory())
    # you can convert that object to a dictionary 
    dict(psutil.virtual_memory()._asdict())
except Exception as err:
    print(err)
    print(sys.exc_info())


#11. Write a Python program to create 100 directories in the current directory.


import os
import sys
try:
    for val in range(1,100):
        os.mkdir("dir" + str(val))
except Exception as err:
    print(err)
    print(sys.exc_info())


#12. Write a Python program to create 100 directories in D:\ or \tmp( if using Linux)

import os
import sys
try:
    path = "D:\\"
    os.chdir(path)
    for val in range(1,100):
        os.mkdir("dir" + str(val))
except Exception as err:
    print(err)
    print(sys.exc_info())
    
#13. Write a Python program to delete some directory and before deleting ONLY if the directory is empty.

import os
import sys
try:
    path = "C:\\Users\\sreevalli kurla ksv\\dir1"
    files = os.listdir(path)
    if len(files) == 0:
        os.rmdir(path)
    else:
        print(path, "is not empty")
except Exception as err:
    print(err)
    print(sys.exc_info())

#14. Write a Python program to copy all the .py files from the current directory to /tmp with exception handling.

import os
import shutil
import sys
try:
    path = os.getcwd()
    destination = "/tmp"
    if os.path.isdir(destination):
        for file in os.listdir(path):
            shutil.copy(file,"/tmp")
    else:
        print(destination , "doesn't exist")
except Exception as err:
    print(err)
    print(sys.exc_info())

#15. Write a Python program to move all the .py files from the current directory to /tmp with exception handling.

import os
import shutil
try:
    path = os.getcwd()
    destination = "/tmp"
    if os.path.isdir(destination):
        for file in os.listdir(path):
            shutil.move(file,"/tmp")
    else:
        print(destination , "doesn't exist")
except Exception as err:
    print(err)
    print(sys.exc_info())


#16. Write a Python program to display all the list of files that are present in the current working directory using the subprocess module.

import subprocess
import os
if os.name == "nt":
    command = ['dir']
elif os.name == 'posix':
    command = ["ls","-ltr"]
p = subprocess.Popen(command ,stdout = subprocess.PIPE , stderr = subprocess.STDOUT )
out, err = p.communicate()
out = out.decode()
print(out)


#17. Write a Python program to create a empty file with today's timestamp.

import time
try:
    filename = time.strftime("%d_%b_%Y.txt")
    print(filename)
    
    fobj =  open(filename,"w")
    fobj.close()
except Exception as err:
    print(err)
    print(sys.exc_info())
    
#18. Write a Python program to create an empty file with todayâ€™s timestamp ( using pathlib library)

import time
from pathlib import Path
try:
    filename = time.strftime("%d_%b_%Y.txt")
    print(filename)
    Path(file).touch()
except Exception as err:
    print(err)
    print(sys.exc_info())

#19. Write a Python program to create an empty file with tomorrowâ€™s timestamp

import time
from pathlib import Path
try:
    today = datetime.date.today()
    print('Today:', today)
    tomorrow = today + datetime.timedelta(days=1)
    print('Tomorrow:', tomorrow)
    file = time.strftime(tomorrow + ".txt")
    Path(file).touch()
except Exception as err:
    print(err)
    print(sys.exc_info())

#20.Write a Python program to rename all the .txt files to .log files

import os
import re #for pattern kind
for file in os.listdir():
    if file.endswith(".txt"):
        newfile = re.sub("txt$","log",file)
        os.rename(file, newfile)

# 21. Write a Python to compare 2 directories ( Eg: C:\python36 and c:\python27 ) and display the below information

# -all the common files present in C:\python36 and C:\python27
# -all the distinct files present in both C:\python36 and C:\python27
# -all the files present in C:\python36
# -all the files present in C:\python27

from filecmp import dircmp

# Construct a new directory comparision object
# to compare the directories left and right

dcmp = dircmp(r"C:\Python35",r"C:\Python35")

# This directory from left side of dircmp method
print("\nleft:",dcmp.left)



#Files and subdirectories in a directory from left side of dircmp method
print("\nleft list:", dcmp.left_list)

#The directory from right side of dircmp method
print("\nright:",dcmp.right)

 
#Files and subdirectories in a directory from right side of dircmp method
print("\right list:", dcmp.right_list)

#Files and subdirectories in both left and right
print("\nCommon:",dcmp.common)

#Files in both left and right
print("\nCommon files:", dcmp.common_files)

#files which are identical in both left and right, using the class's
# file comparision operator
print("\nsame_files", dcmp.same_files)


#22. Write a Python program to generate 4 digit random number.

import random
print(random.randrange(1000,9999))

#23. Write a python program to capture 10 numbers from the user, append to the list and shuffle all the numbers and display the output.

from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

#24. Write a Python program to display all the files and its accessed time, modified time, change time, and size in bytes with proper formatted output.



#25. Write a Python program to create zip files with all the .py files present in the current working directory.

#26. Write a Python program to delete all the files from the current directory that are older than 10 days.

def cleanup(number_of_days, path):
    print("Inside cleanup")
    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    if os.path.isdir(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            shutil.rmtree(path)
    elif os.path.isfile(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            remove(path)
directory = os.getcwd()
path_with_days = { directory :10 }
for path,days in path_with_days.items():
    cleanup(days, path)


#27. Write a Python program to delete all the files from the current directory that are not modified in last 10 days.

def cleanup(number_of_days, path):
    print("Inside cleanup")
    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    if os.path.isdir(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            shutil.rmtree(path)
    elif os.path.isfile(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            remove(path)
directory = os.getcwd()
path_with_days = { directory :10 }
for path,days in path_with_days.items():
    cleanup(days, path)


#28. Write a Python program to archive all the files that are older than 100 days from the current directory.



#29. Write a Python program to validate the email-address

# – using regular expression
# – without regular expression

# Expected output
# Enter Email Address : giridhar276@gmail.com
# Valid mail id

# Enter Email Address : hello#gmail.com
# Invalid mail id

# Enter Email address L hello@gmail
# Invalid mail id

import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = "giridhar276@gmail.com"
if re.search(regex,email):
    print("valid email")
else:
    print("Invalid email")

## 2nd example
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = "giridhar276@gmail.com"
if re.search(regex,email):
    print("valid email")
else:
    print("Invalid email")
    
    
#30. Write a Python program to validate the IP Address

# without regex
ip = input("Enter any ip address:")
out = ip.split(".")
ip = input("Enter any ip address:")
out = ip.split(".")
if len(out) != 4 :
    print("Invalid ip")   
if int(out[0])  in range(1,256) and int(out[1])   in range(0,256) and  int(out[2])   in range(0,256) and  int(out[3])   in range(0,256):
    print("Valid ip")
else:
    print("Invalid ip")    


#31. Write a Python Program to ping ‘www.google.com’ domain and check it is reachable or not.


#32. Write a program to automate the pip installation process using the script.



   

 

