def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b# 意为a=b; b=a+b;
        n = n + 1
    return 'done'


print(fib(6))
 

#最难理解的就是generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#举个简单的例子，定义一个generator，依次返回数字1，3，5：

def odd():
    print('step 1')
    yield(1)
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b #一个generator
        #定义generator的另一种方法。
        #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
        #而是一个generator：
        a, b = b, a + b
        n = n + 1
    return 'done'
