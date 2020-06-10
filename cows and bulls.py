from random import randint
v=randint(1000,9999)
print(v)
q=list(str(v))
s=list(input())
if(q==s):
    print("You have won")
else:
    m=[]
    p=[]
    c=b=0
    d=4
    for i in range(d):
        if s[i]==q[i]:
            c+=1
        else:
            m.append(q[i])
            p.append(s[i])
    c1=len(m)
    for i in range(c1):
        for j in range(c1):
            if m[i]==p[j]:
                b+=1
    if(c==1 and b==1):
        print(str(c)+" cow,"+str(b)+" bull")
    elif(c==1 and b>1):
        print(str(c)+" cow,"+str(b)+" bulls")
    elif(c>1 and b==1):
        print(str(c)+" cows,"+str(b)+" bull")
    else:
        print(str(c)+" cows,"+str(b)+" bulls")

