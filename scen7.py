# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:41:04 2020

@author: Shashwat Sharma
"""



def check_prime(num):
    flag = 0
    for i in range(2,num,1):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        return flag,num
    else:
        return flag,num
    


# reading files

file = open('one.txt','r')
file1_content = file.read()
file = open('two.txt','r')
file2_content = file.read()


list_file1 = file1_content.split(',')
list_file2 = file2_content.split(',')

#converting strings to integers

for i in range(0,len(list_file1),1):
    list_file1[i] = int(list_file1[i])

for i in range(0,len(list_file2),1):
    list_file2[i] = int(list_file2[i])
    
prime_list1 = []
prime_list2 = []

for i in range(0,len(list_file1),1):
    status,res = check_prime(list_file1[i])
    if status == 0:
        prime_list1.append(res)
    elif status == 1:
        continue

for i in range(0,len(list_file2),1):
    status,res = check_prime(list_file2[i])
    if status == 0:
        prime_list2.append(res)
    elif status == 1:
        continue
    
result = []

for item in prime_list1:
    result.append(item)

for i in range(0,len(prime_list1),1):
    if prime_list1[i] in prime_list2:
        continue
    else:
        prime_list2.append(prime_list1[i])
        
prime_list2.sort()

print("\nThe result is:")

len_res = len(prime_list2)
for i in range(0,len_res,1):
    prime_list2[i] = str(prime_list2[i])
    
string_1 = ','.join(prime_list2)
print(string_1)

# write to file
file_write = open('output1.txt','w')
file_write.write(string_1)

file_write.close()
file.close()