def fib(n):
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
fib(2)

# def fib(num):
#     a=0
#     b=1
#     if num<=0:
#         print("Invalid input")
#     elif num== 1:
#         print(a)
#     elif num==2:
#         print(a,b, end=" ")
#     else:
#         print(a,b, end=" ")
#         for i in range (num-2):
#             c = a+b
#             a=b
#             b=c
#             print(c,end=" ")
#
# fib(8)
