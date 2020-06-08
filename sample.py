# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:24:32 2020

@author: Shashwat Sharma
"""

from sys import argv
print("The file1 name is :",argv[1])
print("The file2 name is :",argv[2])

# file opening and reading data

file1 = argv[1]
file2 = argv[2]

file = open(file1,"r")
file1_content = file.read()
file = open(file2,"r")
file2_content = file.read()
print()


# splitting file content and storing them as lists in appropriate format
list_file1 = file1_content.split(',')
list_file2 = file2_content.split(',')


length_file1  = len(list_file1)
length_file2  = len(list_file2)


for i in range(0,length_file1,1):
    try:    
        list_file1[i] = int(list_file1[i])
    except ValueError:
        print(file1,"file contains an invalid literal which is an alphabet.")
    
for i in range(0,length_file2,1):
    try:    
        list_file2[i] = int(list_file2[i])
    except ValueError:
        print(file2,"file contains an invalid literal which is an alphabet.")


print()
print("The file content are as follows: ")
print(list_file1)
print(list_file2)
print()


# division operation takes place

list_result = []

for i in range(0,length_file1,1):
    try:
        result = list_file1[i] / list_file2[i]
        list_result.append(result)
    except TypeError:
        print("For Division both literals have to be a number")
    except ZeroDivisionError:
        print("You cannot divide a number by 0")
    
    

# storing the result as a string
print("\nThe result is:")

len_res = len(list_result)
for i in range(0,len_res,1):
    list_result[i] = str(list_result[i])
    
string_1 = ','.join(list_result)
print(string_1)


#save the result in a file known as output.txt

file_result = open('output.txt','w')

file_result.write(string_1)

file_result.close()
file.close()
