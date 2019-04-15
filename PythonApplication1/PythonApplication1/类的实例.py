class Test: #通过class来定义类 Test为类名 
    #通常格式 class test(obj):  (obj)意为当前test类是从obj这个类中继承的
    def prt(self):
        print(self)
        print(self.__class__)
t=Test()
t.prt()
#类的方法和普通函数区别在于有个第一参数名称,通常是self
#self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类
