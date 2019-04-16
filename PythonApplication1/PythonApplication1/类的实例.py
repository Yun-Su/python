class Test: #通过class来定义类 Test为类名 
    #通常格式 class test(obj):  (obj)意为当前test类是从obj这个类中继承的
    def prt(self):
        #类的方法和普通函数区别在于有个第一参数名称,通常是self
        print(self)#self 代表的是类的实例，代表当前对象的地址
        print(self.__class__)#self.class则指向类
t=Test()
t.prt()