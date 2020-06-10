# BOX 1
def func(s,q):
    for i in range(q//3):
        print("|",end=" ")
        for j in range(q//3):
            print(s,end=" | ")
            s+=1
        print()

# BOX 2
def func1(s,q):
    for i in range(3):
        print("|",end=" ")
        for j in range(3):
            print(chr(s),end=" | ")
            s+=1
        print()



print("Box 1:")
func(1,10)
print()
print("Box 2:")
func1(65,75)
