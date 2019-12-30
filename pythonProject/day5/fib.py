"""
fib
"""
def fib(n):
    a,b=1,1
    while a < n:
        print(a,end=' ')
        a,b = b, a+b

num = int(input("请输入上限值："))
fib(num)

"""
def fib_1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fib_1(n-1)+fib_1(n-2)
num = int(input("请输入上限值："))
fib_1(num)
"""
