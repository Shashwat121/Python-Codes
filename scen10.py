# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:48:44 2020

@author: Shashwat Sharma
"""


from sys import argv
print("First number is: ",argv[1])
print("Second number is: ",argv[2])

#sum = argv[1] + argv[2]
# here the code doesn't give right output because commandline arguments are strings by type

n1 = int(argv[1])
n2 = int(argv[2])
sum = n1 + n2
print(sum)

s1 = argv[3]
s2 = argv[4]

sum1 = s1 + s2
print(sum1)

print(argv[5],argv[7])
print(len(argv))
print(argv[0])
print(type(argv))