#判断一个对象的类型和方法可以使用type()
#返回对应的Class类型
print(type(123))
#<class 'int'>
print(type('abc')==type('123'))

#判断一个对象是否是class类型

class a(object):
    pass
class b(a):
    pass
class c(b):
    pass

a1=a()
b1=b()
c1=c()

print("isinstance:",isinstance(c1,c))
#打印出True因为c1变量指向的就是C这个类。
print("isinstance:",isinstance(c1,a))
#打印出True因为c1变量继承自a这个类 
#isinstance()判断的是一个对象是否是该类型本身
#或者位于该类型的父继承链上。
