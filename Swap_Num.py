# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:34:37 2020

@author: Shashwat Sharma
"""


def count_digits(num):
    count = 0
    while num>0:
        num = num //10
        count = count + 1
    return count



def swapnum(num):
    num_list = []
    while num>0:
        rem = num % 10
        num_list.append(rem)
        num = num // 10
    temp = num_list[0]
    num_list[0] = num_list[3]
    num_list[3] = temp
    
    result = num_list[0] * 1000 + num_list[1] * 100 + num_list[2] * 10 + num_list[3]
    return result   
        

# read file from data.txt

file = open('data.txt','r')
file_content = file.read()

result_list = []

list_content = file_content.split('\n')


for i in range(0,len(list_content),1):
    list_content[i] = int(list_content[i])
    
print("Input data:")
print(list_content)
print()

for i in range(0,len(list_content),1):
    res = count_digits(list_content[i])
    if res == 4:
        swap_res = swapnum(list_content[i])
        result_list.append(swap_res)
    elif res!=4:
        result_list.append(list_content[i])

print("Output data on swapping the middle digits for a 4 digit number only")
print(result_list)
