def my_abs(x):#defind一个自定义函数
    if x >= 0:
        return x
    else:
        return -x

#定义一个什么事也不做的空函数，可以用pass语句：

def nop():
    pass
#pass语句可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#就可以先放一个pass，让代码能运行起来。
def p(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(p(3,3))