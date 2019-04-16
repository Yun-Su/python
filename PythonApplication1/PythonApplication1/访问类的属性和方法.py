#!/usr/bin/python3
class MyClass:
    #一个简单的类的实例
    i = 12345
    def f(self):
        return 'hello world'

# 实例化的类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())



#使用构造方法调用实例化以后的类
#定义了__init__()的特殊(构造方法)
#仅在类实例化以后才会自动调用
#_ _ init_ _ 这是两根连续的横线
#!/usr/bin/python3
class Complex:
    def __init__(a, b, c):
        a.y= b
        a.z= c
x = Complex(3.0, -4.5)
print(x.y, x.z)   
# 输出结果：3.0 -4.5