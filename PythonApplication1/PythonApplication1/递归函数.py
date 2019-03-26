def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print('10的阶乘是',fact(10))
#1*2*3*4*5.....*N
#递归函数的优点是定义简单，逻辑清晰。
#理论上，所有的递归函数都可以写成循环的方式，
#但循环的逻辑不如递归清晰。
#使用递归函数需要注意防止栈溢出。
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

#尾递归方式解决栈溢出
def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#                    4,5*1
#                    3,4*5
#                    2,3*4*5
#                    1,2*3*4*5
#                    num==1, return 上次传入的product
print(fact1(5))
