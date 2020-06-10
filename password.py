"""
Scenario 2:Write a python program to find out the given password is valid for below condition.
                a. Password length should be between 8 to 10.
                b. Password should be alpha numeric
                c. Password should not start or end with number.
                d. Password should not start or end with upper cases character
"""
password=input()
length=len(s)
if(n>=8 and n<=10):
    if password.isalnum():
        if(password[0].islower() and password[length-1].islower()):
                print("valid password")
        else:
            print("Entered password is invalid")
    else:
        print("Entered password is invalid")
else:
    print("Entered password is invalid")
