try:
    for i in['a','b','c']:
        print(i**2)
except TypeError:
    print("Operand type is not supported!!!")
while True:
    try:
        def func_sqr(k):
            l=k*k
            return l
        num=int(input())
        r=func_sqr(num)
    except ValueError:
        print("Incorrect input is entered!!")
    else:
        print(r)
