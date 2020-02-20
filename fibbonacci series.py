'''def fib(n):
    a=0
    b=1
    if n<= 0:
        print("Input is invalid")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range (2,n):
            c = a+b
            a=b
            b=c
            print(c)
fib(-2) '''

def fib(sum):
    a=0
    b=1
    if sum<0:
        print("Invalid input")
    elif sum== 0:
        print(a)
    elif sum==1:
        print(a)
        print(b)
    else:
        print(a)
        print(b)

        for i in range (1,sum):
            c = a+b
            a=b
            b=c
            if(c<=sum):
                 print(c)

fib(50)
