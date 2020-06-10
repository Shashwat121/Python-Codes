import math
list1=[("Mumbai",6817),("Chennai",1389),("Delhi",2514),("Gujarat",2815),("Kolkatta",1061),("Banglore",2034)]
a=int(input("How many metros you want to add:"))
for i in range(a):
    x=input()
    y=int(input())
    list1.append((x,y))
print(list1)
sum1=c=0
for i in range(0,len(list1)):
    sum1=sum1+(list1[i][1])
    c+=1
a=math.ceil(sum1/c)
k=[]
g=0
for i in range(0,len(list1)):
    if list1[i][1]>a:
        print(list1[i][0],":Red Zone Need to be sealed")
        k.append(list1[i][0])
        g+=1
    elif list1[i][1]<=a/2:
        print(list1[i][0],":Orange Zone Need to be Quarantine")
    else:
        print(list1[i][0],":Stay home Stay safe")
print("Number of cases more than average is {0} and the cities are".format(g))
for i in range(0,len(k)):
    print(k[i])
